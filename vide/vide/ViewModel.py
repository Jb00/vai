from videtoolkit import core
from . import flags
from .positions import DocumentPos

class ViewModel(core.VObject):
    def __init__(self):
        super(ViewModel, self).__init__()
        self._editor_mode = flags.COMMAND_MODE
        self._document_pos_at_top = DocumentPos(1,1)
        self._badges = {}
        self.modeChanged = core.VSignal(self)
        self.documentPosChanged = core.VSignal(self)
        self.badgeChanged = core.VSignal(self)

    def editorMode(self):
        return self._editor_mode

    def setEditorMode(self, mode):
        self._editor_mode = mode
        self.modeChanged.emit(self._editor_mode)

    def documentPosAtTop(self):
        return self._document_pos_at_top

    def setDocumentPosAtTop(self, doc_pos):
        self._document_pos_at_top = doc_pos
        self.documentPosChanged.emit()

    def addBadge(self, doc_line, badge):
        self._badges[doc_line] = badge
        self.badgeChanged.emit()

    def badge(self, doc_line):
        return self._badges.get(doc_line)

