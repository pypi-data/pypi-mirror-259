import re
import fnmatch
import functools

from qtpy import QtGui, QtWidgets, QtCore
from qtpy.QtCore import Signal

from ._qt import load_ui
from .plot import NDScopePlotChannel

# ------------------------------------------------------------------------------

COLOR_TESTPOINT = 'blue'
COLOR_ONLINE = 'green'


def brush_for_channel(channel):
    if channel.testpoint:
        return QtGui.QBrush(QtGui.QColor(COLOR_TESTPOINT))
    elif channel.online:
        return QtGui.QBrush(QtGui.QColor(COLOR_ONLINE))
    else:
        return QtGui.QBrush()

# ------------------------------------------------------------------------------

def is_slow(sample_rate):
    return sample_rate <= 16

def is_fast(sample_rate):
    return not is_slow(sample_rate)

# ------------------------------------------------------------------------------

def filter_channel(channel, show_slow, show_fast, show_online_only):
    if show_online_only and not channel.online:
        return False
    else:
        if show_slow and is_slow(channel.sample_rate):
            return True
        elif show_fast and is_fast(channel.sample_rate):
            return True
        else:
            return False

# ------------------------------------------------------------------------------

class AvailableChannelTreeItem:
    def __init__(self, parent=None, data=None, is_leaf=False):
        self.parent = parent
        self.data = data
        self.is_leaf = is_leaf
        if not is_leaf:
            self.branch_dict = {}
            self.leaf_dict = {}

            self.has_slow = False
            self.has_slow_online = False
            self.has_fast = False
            self.has_fast_online = False

    def child_list(self):
        if not self.is_leaf:
            return list(self.branch_dict.values()) + list(self.leaf_dict.values())
        return []

    def row(self):
        if self.parent:
            return self.parent.child_list().index(self)
        else:
            return 0


class AvailableChannelTreeModel(QtCore.QAbstractItemModel):
    def __init__(self, channel_list, max_depth=4):
        super().__init__()
        self.header_role_data = {QtCore.Qt.DisplayRole: ('name', 'rate')}
        self.root = AvailableChannelTreeItem()
        self.max_depth = max_depth
        self.insert(channel_list)

    def insert(self, channel_list):
        # HACK: there's something weird about the matching of this
        # character set.  If the underscore is at the end of the set,
        # e.g. '[:-_]', then the matches are wrong.  Is this a bug in
        # python???
        split_re = re.compile(r'[_:-]')
        for channel in channel_list:
            current = self.root
            slow = is_slow(channel.sample_rate)
            online = channel.online
            name_part_list = split_re.split(channel.name, self.max_depth)
            for name_part in name_part_list[:-1]:
                if name_part not in current.branch_dict:
                    current.branch_dict[name_part] = AvailableChannelTreeItem(current, name_part)
                current = current.branch_dict[name_part]
                if slow:
                    current.has_slow = True
                    if online:
                        current.has_slow_online = True
                else:
                    current.has_fast = True
                    if online:
                        current.has_fast_online = True
            current.leaf_dict[channel.name] = AvailableChannelTreeItem(current, channel, is_leaf=True)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.header_role_data[QtCore.Qt.DisplayRole])

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return QtCore.QVariant()

        item = index.internalPointer()
        if item.is_leaf:
            channel = item.data
            brush = brush_for_channel(channel)
            sample_rate = f'{float(channel.sample_rate):g}'
            role_data = {QtCore.Qt.DisplayRole: (channel.name, sample_rate),
                         QtCore.Qt.ForegroundRole: (brush, brush)}
        else:
            name_part = item.data
            role_data = {QtCore.Qt.DisplayRole: (name_part, '')}

        try:
            return role_data[role][index.column()]
        except KeyError:
            return QtCore.QVariant()
        except IndexError:
            return QtCore.QVariant()

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags

        item = index.internalPointer()
        if item.is_leaf:
            flags = (
                QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemNeverHasChildren,
                QtCore.Qt.ItemIsEnabled)
        else:
            flags = (QtCore.Qt.ItemIsEnabled, QtCore.Qt.ItemIsEnabled)

        try:
            return flags[index.column()]
        except IndexError:
            return QtCore.Qt.NoItemFlags

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal:
            try:
                return self.header_role_data[role][section]
            except KeyError:
                return QtCore.QVariant()
            except IndexError:
                return QtCore.QVariant()

        return QtCore.QVariant()

    def index(self, row, column, parent=QtCore.QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        try:
            child_item = parent_item.child_list()[row]
            return self.createIndex(row, column, child_item)
        except IndexError:
            return QtCore.QModelIndex()

    def mimeData(self, indexes):
        text_list = [self.data(index, QtCore.Qt.DisplayRole) for index in indexes if index.isValid()]
        text = '\n'.join(text_list)
        mime_data = QtCore.QMimeData()
        mime_data.setText(text)
        return mime_data

    def mimeTypes(self):
        return ['text/plain']

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent
        if parent_item == self.root:
            return QtCore.QModelIndex()

        row = parent_item.row()
        return self.createIndex(row, 0, parent_item)

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parent_item = self.root
        else:
            parent_item = parent.internalPointer()

        return len(parent_item.child_list())


# Filters the branch and leaf items based on the sample rate and online status
# of the channels that they contain.
class AvailableChannelTreeSortFilterProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.show_slow = True
        self.show_fast = True
        self.show_online_only = False

    def filterAcceptsRow(self, source_row, source_parent):
        index = self.sourceModel().index(source_row, 0, source_parent)
        item = index.internalPointer()
        if item.is_leaf:
            channel = item.data
            return filter_channel(channel, self.show_slow, self.show_fast, self.show_online_only)
        else:
            if self.show_online_only:
                if self.show_slow and item.has_slow_online:
                    return True
                elif self.show_fast and item.has_fast_online:
                    return True
                else:
                    return False
            else:
                if self.show_slow and item.has_slow:
                    return True
                elif self.show_fast and item.has_fast:
                    return True
                else:
                    return False


class AvailableChannelTreeView(QtWidgets.QTreeView):
    def __init__(self, parent):
        super().__init__(parent)


class AvailableChannelTableModel(QtCore.QAbstractTableModel):
    def __init__(self, channel_list, parent=None):
        super().__init__(parent)
        self.search_pattern = ''
        self.show_slow = True
        self.show_fast = True
        self.show_online_only = False

        self.full_channel_list = channel_list
        self.filtered_channel_list = channel_list
        self.header_data = ('name', 'rate')

    def columnCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.header_data)

    def data(self, index, role):
        try:
            channel = self.itemFromIndex(index)
        except IndexError:
            return QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole:
            return (channel.name, str(channel.sample_rate))[index.column()]
        elif role == QtCore.Qt.ForegroundRole:
            return brush_for_channel(channel)
        else:
            return QtCore.QVariant()

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.NoItemFlags
        try:
            return (
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemNeverHasChildren),
            )[index.column()]
        except IndexError:
            return QtCore.Qt.NoItemFlags

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header_data[section]
        elif orientation == QtCore.Qt.Vertical:
            return section + 1
        else:
            return QtCore.QVariant()

    def itemFromIndex(self, index):
        return self.filtered_channel_list[index.row()]

    def mimeData(self, indexes):
        text_list = [self.data(index, QtCore.Qt.DisplayRole) for index in indexes if index.isValid()]
        text = '\n'.join(text_list)
        mime_data = QtCore.QMimeData()
        mime_data.setText(text)
        return mime_data

    def mimeTypes(self):
        return ['text/plain']

    def rowCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.filtered_channel_list)

    def update_filter(self):
        # FIXME: this is fairly slow, how can we speed this up?
        def _match(channel):
            return \
                filter_channel(channel, self.show_slow, self.show_fast, self.show_online_only) \
                and (
                    self.search_pattern in channel.name \
                    or fnmatch.fnmatch(channel.name, self.search_pattern)
                )
        filtered_channel_list = [
            chan for chan in self.full_channel_list if _match(chan)
        ]
        self.beginResetModel()
        self.filtered_channel_list = filtered_channel_list
        self.endResetModel()


class AvailableChannelTableView(QtWidgets.QTableView):
    def __init__(self, parent):
        super().__init__(parent)


class ChannelListWidget(*load_ui('channel_list.ui')):

    def __init__(self, available_channel_tree_model, available_channel_table_model, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # available channel tree model
        self.available_channel_tree_model = available_channel_tree_model
        self.available_channel_tree_proxy_model = AvailableChannelTreeSortFilterProxyModel()
        self.available_channel_tree_proxy_model.setSourceModel(self.available_channel_tree_model)

        # available channel tree view
        self.available_channel_tree_view.setModel(self.available_channel_tree_proxy_model)
        self.available_channel_tree_view.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.available_channel_tree_view.header().setSectionsMovable(False)
        self.available_channel_tree_view.setDragEnabled(True)
        self.available_channel_tree_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # available channel table model
        self.available_channel_table_model = available_channel_table_model

        # available channel table view
        self.available_channel_table_view.setModel(self.available_channel_table_model)
        self.available_channel_table_view.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.available_channel_table_view.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.available_channel_table_view.horizontalHeader().setHighlightSections(False)
        self.available_channel_table_view.setDragEnabled(True)
        self.available_channel_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.available_channel_table_view.setWordWrap(False)

        self.all_radio_button.toggled.connect(self.all_radio_button_toggled_slot)
        self.slow_radio_button.toggled.connect(self.slow_radio_button_toggled_slot)
        self.fast_radio_button.toggled.connect(self.fast_radio_button_toggled_slot)

        self.online_checkbox.setStyleSheet('color: {0}'.format(COLOR_ONLINE))
        self.online_checkbox.stateChanged.connect(self.online_checkbox_state_changed_slot)

        self.search_line_edit.textChanged.connect(self.search_line_edit_text_changed_slot)
        self.search_line_edit.setClearButtonEnabled(True)
        self.search_line_edit.setFocus()

        # FIXME: this is a substitute (possibly) for logic that should
        # maybe be based on whether we're talking to an NDS1 or NDS2
        # server.  for NDS1 everything is online, and there are
        # testpoints (which are also online only), so a checkbox to
        # filter on online is superfulous.
        all_online = functools.reduce(
            lambda value, chan: value and chan.online,
            self.available_channel_table_model.full_channel_list,
            True,
        )
        if all_online:
            self.online_checkbox.hide()
            # FIXME: this should be based on the presence of test points
            self.legendLabel.setText(f"<span style='color: {COLOR_TESTPOINT}'>testpoints in blue</span>")
        else:
            self.legendLabel.hide()

    def set_server_info(self, server, nchannels, glob=None):
        text = f"server: <span style='font-weight: bold'>{server}</span>"
        text += f" [{nchannels} channels]"
        if glob and glob != '*':
            text += f" (channel glob: '{glob}')"
        self.title.setText(text)

    def search_line_edit_text_changed_slot(self, text):
        self.available_channel_table_model.search_pattern = text
        self.available_channel_table_model.update_filter()

    def all_radio_button_toggled_slot(self, checked):
        if checked:
            self.available_channel_tree_proxy_model.show_slow = True
            self.available_channel_tree_proxy_model.show_fast = True
            self.available_channel_tree_proxy_model.invalidateFilter()

            self.available_channel_table_model.show_slow = True
            self.available_channel_table_model.show_fast = True
            self.available_channel_table_model.update_filter()

    def slow_radio_button_toggled_slot(self, checked):
        if checked:
            self.available_channel_tree_proxy_model.show_slow = True
            self.available_channel_tree_proxy_model.show_fast = False
            self.available_channel_tree_proxy_model.invalidateFilter()

            self.available_channel_table_model.show_slow = True
            self.available_channel_table_model.show_fast = False
            self.available_channel_table_model.update_filter()

    def fast_radio_button_toggled_slot(self, checked):
        if checked:
            self.available_channel_tree_proxy_model.show_slow = False
            self.available_channel_tree_proxy_model.show_fast = True
            self.available_channel_tree_proxy_model.invalidateFilter()

            self.available_channel_table_model.show_slow = False
            self.available_channel_table_model.show_fast = True
            self.available_channel_table_model.update_filter()

    def online_checkbox_state_changed_slot(self, state):
        if state == QtCore.Qt.Unchecked:
            self.available_channel_tree_proxy_model.show_online_only = False
            self.available_channel_tree_proxy_model.invalidateFilter()

            self.available_channel_table_model.show_online_only = False
            self.available_channel_table_model.update_filter()
        elif state == QtCore.Qt.Checked:
            self.available_channel_tree_proxy_model.show_online_only = True
            self.available_channel_tree_proxy_model.invalidateFilter()

            self.available_channel_table_model.show_online_only = True
            self.available_channel_table_model.update_filter()


# ------------------------------------------------------------------------------


class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self):
        super().__init__()

    def paint(self, painter, option, index):
        button = QtWidgets.QStyleOptionButton()
        button.text = '-'
        button.rect = option.rect
        button.rect.setWidth(min(option.rect.width(), 30))
        button.state = QtWidgets.QStyle.State_Enabled
        QtWidgets.QApplication.style().drawControl(QtWidgets.QStyle.CE_PushButton, button, painter)


class ConfigChannelTableModel(QtCore.QAbstractTableModel):
    # items in table are NDScopePlotChannel items.  setItemList
    # expects a list of PlotChannel objects, but all other
    # inserts/append operations expect channel name strings.

    def __init__(self, parent=None):
        super().__init__(parent)
        self.item_list = []
        self.header = ('', 'name', 'color', 'width', 'scale', 'offset', 'unit', 'label')

    def __contains__(self, name):
        """check that channel name already in table or not"""
        for channel in self.item_list:
            if channel.channel == name:
                return True
        return False

    def _make_item(self, name):
        """make a table item from a channel name string"""
        return NDScopePlotChannel(name)

    def canDropMimeData(self, data, action, row, column, parent):
        return data.hasFormat('text/plain')

    def columnCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.header)

    def data(self, index, role):
        try:
            item = self.item_list[index.row()]
        except IndexError:
            return QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            column_data = (
                '',
                item.channel,
                '',
                item.params['width'],
                item.params['scale'],
                item.params['offset'],
                item.params['unit'],
                item.params['label'],
            )
            return column_data[index.column()]
        elif role == QtCore.Qt.ForegroundRole:
            return QtGui.QBrush()
        elif role == QtCore.Qt.BackgroundRole and index.column() == 2:
            return item.get_QColor()
        elif role == QtCore.Qt.ToolTipRole and index.column() == 0:
            return 'remove channel'
        else:
            return QtCore.QVariant()

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsDropEnabled
        try:
            return (
                (QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemNeverHasChildren),
                (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemNeverHasChildren),
            )[index.column()]
        except IndexError:
            return QtCore.Qt.NoItemFlags

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[section]
        elif orientation == QtCore.Qt.Vertical:
            return section + 1
        else:
            return QtCore.QVariant()

    def dropMimeData(self, data, action, row, column, parent):
        if data.hasFormat('text/plain'):
            text = data.text()
            text_list = text.splitlines()

            item_list = [self._make_item(text) for text in text_list if text not in self]
            count = len(item_list)

            if count > 0:
                if row == -1 and column == -1:
                    if not parent.isValid():
                        # Drop is after last row.
                        row = len(self.item_list)
                        self.beginInsertRows(QtCore.QModelIndex(), row, row + count - 1)
                        for i in range(count):
                            self.item_list.insert(row + i, item_list[i])
                        self.endInsertRows()
                        return True
                    else:
                        # Drop is on row.
                        row = parent.row()
                        self.item_list[row] = item_list.pop(0)
                        row = row + 1
                        count = count - 1
                        self.beginInsertRows(QtCore.QModelIndex(), row, row + count - 1)
                        for i in range(count):
                            self.item_list.insert(row + i, item_list[i])
                        self.endInsertRows()
                        return True
                elif row >= 0 and column >= 0:
                    # Drop is before first row or between rows.
                    self.beginInsertRows(QtCore.QModelIndex(), row, row + count - 1)
                    for i in range(count):
                        self.item_list.insert(row + i, item_list[i])
                    self.endInsertRows()
                    return True
                else:
                    return False
            else:
                return False

    def mimeData(self, indexes):
        text_list = [self.data(index, QtCore.Qt.DisplayRole) for index in indexes if index.isValid()]
        text = '\n'.join(text_list)
        mime_data = QtCore.QMimeData()
        mime_data.setText(text)
        return mime_data

    def mimeTypes(self):
        return ['text/plain']

    def rowCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.item_list)

    def supportedDropActions(self):
        return (QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)

    def getItemList(self):
        """get list of PlotChannel objects in the table"""
        return self.item_list

    def setItemList(self, item_list):
        """set the list of PlotChannel objects in the table"""
        self.item_list = item_list

    def removeRows(self, row, count, parent=QtCore.QModelIndex()):
        if count <= 0 or row < 0 or (row + count) > self.rowCount(parent):
            return False
        self.beginRemoveRows(QtCore.QModelIndex(), row, row + count - 1)
        for i in range(count):
            del self.item_list[row + i]
        self.endRemoveRows()
        return True

    def removeRow(self, row, parent=QtCore.QModelIndex()):
        return self.removeRows(row, 1, parent)

    def setData(self, index, value, role):
        if index.isValid() and role == QtCore.Qt.EditRole:
            if index.column() == 3:  # width
                if value > 0:
                    self.item_list[index.row()].set_params(width=value)
                    self.dataChanged.emit(index, index, [role])
                    return True
                else:
                    return False
            elif index.column() == 4:  # scale
                self.item_list[index.row()].set_params(scale=value)
                self.dataChanged.emit(index, index, [role])
                return True
            elif index.column() == 5:  # offset
                self.item_list[index.row()].set_params(offset=value)
                self.dataChanged.emit(index, index, [role])
                return True
            elif index.column() == 6:  # unit
                self.item_list[index.row()].set_params(unit=value)
                self.dataChanged.emit(index, index, [role])
                return True
            elif index.column() == 7:  # label
                self.item_list[index.row()].set_params(label=value)
                self.dataChanged.emit(index, index, [role])
                return True
            else:
                return False
        else:
            return False

    def setItemData(self, index, roles):
        if QtCore.Qt.EditRole in roles.keys():
            return self.setData(index, roles[QtCore.Qt.EditRole], QtCore.Qt.EditRole)
        elif QtCore.Qt.DisplayRole in roles.keys():
            return self.setData(index, roles[QtCore.Qt.DisplayRole], QtCore.Qt.DisplayRole)
        else:
            return False

    def add_channel(self, name):
        """add a channel to the table by name"""
        if name in self:
            return
        row = len(self.item_list)
        self.beginInsertRows(QtCore.QModelIndex(), row, row)
        self.item_list.insert(row, self._make_item(name))
        self.endInsertRows()


class ConfigChannelTableView(QtWidgets.QTableView):
    def __init__(self, parent):
        super().__init__(parent)
        self.color_dialog = QtWidgets.QColorDialog()
        self.color_dialog.setModal(True)
        self.clicked.connect(self.clicked_slot)

    def clicked_slot(self, index):
        if index.column() == 0:
            model = self.model()
            model.removeRow(index.row())
        elif index.column() == 2:
            model = self.model()
            item = model.item_list[index.row()]
            color = item.get_QColor()
            self.color_dialog.setCurrentColor(color)
            self.color_dialog.colorSelected.connect(lambda color: self.color_selected_slot(color, item))
            self.color_dialog.show()

    def color_selected_slot(self, color, item):
        self.color_dialog.colorSelected.disconnect()
        item.set_params(color=color.name())


class ChannelConfigWidget(*load_ui('channel_config.ui')):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # selected channel table model
        self.channel_table_model = ConfigChannelTableModel()

        # selected channel table view
        self.channel_table_view.setModel(self.channel_table_model)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.channel_table_view.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.channel_table_view.horizontalHeader().setHighlightSections(False)
        self.channel_table_view.setDragEnabled(True)
        self.channel_table_view.setAcceptDrops(True)
        self.channel_table_view.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.channel_table_view.setDragDropOverwriteMode(False)
        self.channel_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.channel_table_view.setWordWrap(False)
        self.push_button_delegate = PushButtonDelegate()
        self.channel_table_view.setItemDelegateForColumn(0, self.push_button_delegate)

    def set_channel_list(self, channel_list):
        self.channel_table_model.setItemList(channel_list)

    def add_channel(self, channel):
        self.channel_table_model.add_channel(channel)

    def get_channel_list(self):
        return self.channel_table_model.getItemList()


# ------------------------------------------------------------------------------


class ChannelListDialog(QtWidgets.QDialog):
    """modeless dialog to show the channel list

    """
    def __init__(self, channel_list_widget, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QtWidgets.QLabel("NDS Channel List")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.channel_list_widget = channel_list_widget
        self.channel_list_widget.setParent(self)
        self.layout.addWidget(self.channel_list_widget)

        self.foot_layout = QtWidgets.QHBoxLayout()
        self.layout.addLayout(self.foot_layout)

        self.foot_layout.addWidget(QtWidgets.QLabel("Drag channels into plot to add."))
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.buttons()[0].setDefault(False)
        self.buttonBox.buttons()[0].setAutoDefault(False)
        self.buttonBox.rejected.connect(self.reject)
        self.foot_layout.addWidget(self.buttonBox)


class PlotChannelConfigDialog(*load_ui('channel_config_dialog.ui')):
    """modal dialog to configure the channels for an NDScopePlotItem

    """
    done = Signal('PyQt_PyObject')

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.channel_config_widget = ChannelConfigWidget()
        self.channel_config_widget.setParent(self)
        self.verticalLayout.insertWidget(1, self.channel_config_widget)

        self.dialog_button_box.accepted.connect(self._done_accepted)
        self.dialog_button_box.rejected.connect(self._done_rejected)

    def set_plot(self, plot):
        self.title.setText(f"Configure channels for plot {plot.loc}")
        channel_dict = plot.get_channels()
        self.channel_config_widget.set_channel_list(
            [NDScopePlotChannel(chan, **params) for chan, params in channel_dict.items()]
        )

    def _done_accepted(self):
        self.done.emit(self.channel_config_widget.get_channel_list())

    def _done_rejected(self):
        self.done.emit(None)


class ChannelSelectDialog(*load_ui('channel_select_dialog.ui')):

    done = Signal('PyQt_PyObject')

    def __init__(self, channel_list_widget, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.channel_list_widget = channel_list_widget
        self.channel_list_widget.setParent(self)
        self.channel_list_layout.addWidget(self.channel_list_widget)
        self.channel_list_widget.available_channel_tree_view.activated.connect(self.available_channel_tree_view_activated_slot)
        self.channel_list_widget.available_channel_table_view.activated.connect(self.available_channel_table_view_activated_slot)

        self.channel_config_widget = ChannelConfigWidget()
        self.channel_config_widget.setParent(self)
        self.channel_config_layout.addWidget(self.channel_config_widget)

        self.infoLabel.setText(f"Double click or drag channels to select.")

        self.dialog_button_box.accepted.connect(self._done_accepted)
        self.dialog_button_box.rejected.connect(self._done_rejected)

    def setSelectedChannels(self, channel_dict):
        self.channel_config_widget.set_channel_list(
            [NDScopePlotChannel(chan, **params) for chan, params in channel_dict.items()]
        )

    def getSelectedChannelList(self):
        return self.channel_config_widget.get_channel_list()

    def setTitlePlot(self, plot):
        self.title.setText(f"Select/configure channels for plot {plot}")

    # Appends the item in the available channel tree at the supplied
    # index to the end of the selected channel table.
    def available_channel_tree_view_activated_slot(self, index):
        if not self.channel_list_widget.available_channel_tree_proxy_model.hasChildren(index) and index.column() == 0:
            source_index = self.channel_list_widget.available_channel_tree_proxy_model.mapToSource(index)
            item = source_index.internalPointer()
            if item.is_leaf:
                channel = item.data
                self.channel_config_widget.add_channel(channel.name)

    # Appends the item in the available channel table at the supplied
    # index to the end of the selected channel table.
    def available_channel_table_view_activated_slot(self, index):
        if index.column() == 0:
            channel = self.channel_list_widget.available_channel_table_model.itemFromIndex(index)
            self.channel_config_widget.add_channel(channel.name)

    def _done_accepted(self):
        self.done.emit(self.getSelectedChannelList())

    def _done_rejected(self):
        self.done.emit(None)


# ------------------------------------------------------------------------------


def main():
    import os
    import sys
    import signal
    import logging
    import argparse

    from ._qt import create_app
    from . import nds
    from . import const
    from . import util

    logging.basicConfig(
        level=os.getenv('LOG_LEVEL', 'WARNING').upper(),
        format="%(name)s: %(message)s",
    )

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    PROG = 'ndschans'
    DESCRIPTION = 'NDS channel search GUI'

    parser = argparse.ArgumentParser(
        prog=PROG,
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--nds', metavar='HOST[:PORT]',
                        help=f"NDS server [{const.NDSSERVER}]")
    parser.add_argument('glob', nargs='?', default=os.getenv('CHANNEL_GLOB', '*'),
                        help="channel glob to filter channel list (e.g. 'H1:SUS-*')")

    args = parser.parse_args()

    os.environ['NDSSERVER'] = util.resolve_ndsserver(args.nds)

    server, server_formatted = util.format_nds_server_string()

    print(f"Fetching channel list from {server} (channel glob: '{args.glob}')... ")
    channel_dict = nds.find_channels(args.glob)
    channel_list = list(sorted(channel_dict.values(), key=lambda c: c.name))
    nchannels = len(channel_list)
    print(f"Channel list received: {nchannels} channels")

    app = create_app()
    clw = ChannelListWidget(
        AvailableChannelTreeModel(channel_list),
        AvailableChannelTableModel(channel_list),
    )
    clw.set_server_info(server_formatted, nchannels, glob=args.glob)
    cld = ChannelListDialog(clw)
    cld.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
