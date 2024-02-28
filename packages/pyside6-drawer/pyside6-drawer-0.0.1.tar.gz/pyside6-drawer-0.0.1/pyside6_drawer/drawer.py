from PySide6.QtCore import Qt, QPropertyAnimation, QAbstractAnimation, QParallelAnimationGroup, Signal, QEvent
from PySide6.QtWidgets import QWidget, QGridLayout, QGraphicsOpacityEffect
from PySide6.QtGui import QColor, QPalette


class Drawer(QWidget):

    drawerToggled = Signal(bool)

    def __init__(self, 
                 parent, 
                 widget, 
                 alignment: Qt.AlignmentFlag=Qt.AlignmentFlag.AlignLeft):
        super().__init__()  # Make sure parentless
        self.__parent = parent
        self.__widget: QWidget = widget
        self.__drawerAlignment: Qt.AlignmentFlag = alignment
        self.__animator: QParallelAnimationGroup = None
        self.setLayout(QGridLayout())
        self.layout().addWidget(self.__widget, 0, 0, 1, 2, self.__drawerAlignment)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.__initAnimator()
        self.__parent.installEventFilter(self)
        self.setVisible(False)

    @property
    def drawerAlignment(self) -> Qt.AlignmentFlag:
        return self.__drawerAlignment

    def animator(self) -> QParallelAnimationGroup:
        return self.__animator

    def setAnimator(self, group: QParallelAnimationGroup):
        self.__animator = group

    def __initAnimator(self):
        self.setAnimator(QParallelAnimationGroup())
        self.animator().clear()
        if self.drawerAlignment in [Qt.AlignLeft, Qt.AlignRight]:
            prop = b"width"
            sizeCb = self.__widget.setFixedWidth
        elif self.drawerAlignment in [Qt.AlignmentFlag.AlignTop, Qt.AlignBottom]:
            prop = b"height"
            sizeCb = self.__widget.setFixedHeight
        else:
            raise ValueError("Invalid or unsupported alignment flag")
        
        sizeCb(0)
        self.__sizeAnimation = QPropertyAnimation(self, prop)
        self.__sizeAnimation.valueChanged.connect(sizeCb)

        self.__sizeAnimation.setStartValue(0)
        self.__sizeAnimation.setDuration(200)  # Default duration
        self.__sizeAnimation.setEndValue(self.__widget.sizeHint().width())

        self.__opacityAnimation = QPropertyAnimation(self, b"opacity")
        self.__widget.setGraphicsEffect(QGraphicsOpacityEffect(opacity=0.0))
        self.__opacityAnimation.valueChanged.connect(self.__setOpacity)

        self.__opacityAnimation.setStartValue(0.0)
        self.__opacityAnimation.setDuration(200)
        self.__opacityAnimation.setEndValue(1.0)
        
        self.__parentOpacityAnimation = QPropertyAnimation(self, b"parentopacity")
        self.__parentOpacityAnimation.valueChanged.connect(self.__setParentOpacity)

        self.__parentOpacityAnimation.setStartValue(255)
        self.__parentOpacityAnimation.setDuration(200)
        self.__parentOpacityAnimation.setEndValue(127)

        self.animator().addAnimation(self.__sizeAnimation)
        self.animator().addAnimation(self.__opacityAnimation)
        self.animator().addAnimation(self.__parentOpacityAnimation)
        self.animator().stateChanged.connect(self.__animationStateChanged)

    def __animationStateChanged(self, new_state, old_state):
        if new_state == self.animator().State.Running:
            self.__widget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
            self.__parentOpacityAnimation.start()
        elif new_state == self.animator().State.Stopped:
            self.__widget.setAttribute(Qt.WA_TransparentForMouseEvents, False)

    def __setOpacity(self, opacity):
        effect = QGraphicsOpacityEffect(opacity=opacity)
        self.__widget.setGraphicsEffect(effect)

    def __setParentOpacity(self, opacity):
        palette = self.__parent.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255, opacity))
        self.__parent.setPalette(palette)

    def showDrawer(self, show: bool = True):
        if show:
            self.animator().setDirection(QAbstractAnimation.Forward)
        else:
            self.animator().setDirection(QAbstractAnimation.Backward)
        self.animator().start()
    
    def setDuration(self, msecs):
        for a in [self.animator().animationAt(a) for a in range(self.animator().animationCount())]:
            a.setDuration(msecs)

    def setIcon(self, icon):
        assert self.__btn
        self.__btn.setIcon(icon)

    def eventFilter(self, obj, e):
        if isinstance(obj, type(self.__parent)):
            if e.type() == QEvent.MouseButtonRelease:
                if self.__sizeAnimation.currentValue() == self.__sizeAnimation.endValue():
                    self.toggleDrawer()
        return super().eventFilter(obj, e)

    def toggleDrawer(self):
        isVisible = self.isVisible()
        self.setVisible(not isVisible)
        self.showDrawer(not isVisible)
    