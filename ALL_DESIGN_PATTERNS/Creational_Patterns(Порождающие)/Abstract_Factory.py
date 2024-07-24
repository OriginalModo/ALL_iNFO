"""
Абстрактная фабрика (Abstract factory):

Суть: Позволяет создавать семейства связанных между собой обьектов без привязки к их конкретным классам:
Всё взаимодействие происходит через интерфейс базового класса


В каких случаях рекомендуется использовать:
1) Разрабатываемая система не должна зависеть от того, как компонуются, создаются и предоставляются входящие в неё обьекты
2) Обьекты, входящие в взаимосвязанное семейство должны использоваться вместе
3) Конфигурация системы должна производиться одним из семейством составляющих её обьектов
4) Необходимо скрыть от пользователей реализацию, но предоставить интерфейсы для использования модуля (класса, библиотеки)
5) Уже используется Фабричный метод и необходимо ввести в систему новые типы продуктов

Плюсы:
--- гарантирует сочетаемость создаваемых продуктов
--- избавляет клиентский код от привязки к конкретным классам продуктов и упрощает добавление новых
--- выделяет код производства продуктов в одно место, тем самым упрощая поддержку кода

Минусы:
--- Усложнение кода программы, так как добавляется множество дополнительных классов
"""

from abc import ABC, abstractmethod

"""
Базовые классы графического пользовательского интерфейса
"""


class StatusBar(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self):
        pass


class MainMenu(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self):
        pass


class MainWindow(ABC):
    def __init__(self, system: str):
        self._system = system

    @abstractmethod
    def create(self):
        pass


"""
Производные классы графического пользователького интерфейса
для операционной системы Windows
"""


class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__('Windows')

    def create(self):
        print(f"Creared status bar for {self._system}")


class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__('Windows')

    def create(self):
        print(f"Creared MainMenu for {self._system}")


class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__('Windows')

    def create(self):
        print(f"Creared MainWindow for {self._system}")


"""
Производные классы графического пользователького интерфейса
для операционной системы Linux
"""


class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__('Linux')

    def create(self):
        print(f"Creared status bar for {self._system}")


class LinuxMainMenu(MainMenu):
    def __init__(self):
        super().__init__('Linux')

    def create(self):
        print(f"Creared MainMenu for {self._system}")


class LinuxMainWindow(MainWindow):
    def __init__(self):
        super().__init__('Linux')

    def create(self):
        print(f"Creared MainWindow for {self._system}")


"""
Базовый класс абстрактной фабрики
"""


class GuiAbstractFactory(ABC):
    @abstractmethod
    def getStatusBar(self) -> StatusBar:
        pass

    @abstractmethod
    def getMainMenu(self) -> MainMenu:
        pass

    @abstractmethod
    def getMainWindow(self) -> MainWindow:
        pass


"""
Производные классы абстрактной фабрики,
конкретные реализации для каждой из операционных систем
"""


class WindowGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()

    def getMainWindow(self) -> MainWindow:
        return WindowsMainWindow()


class LinuxGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return LinuxStatusBar()

    def getMainMenu(self) -> MainMenu:
        return LinuxMainMenu()

    def getMainWindow(self) -> MainWindow:
        return LinuxMainWindow()


"""
Клиентский класс, использующий фабрику для создания Gui
"""


class Application:
    def __init__(self, factory: GuiAbstractFactory):
        self._gui_factory = factory

    def create_gui(self):
        mainwindow = self._gui_factory.getMainWindow()
        status_bar = self._gui_factory.getStatusBar()
        main_menu = self._gui_factory.getMainMenu()
        mainwindow.create()
        main_menu.create()
        status_bar.create()


def create_factory(system_name: str) -> GuiAbstractFactory:
    factory_dict = {
        'Windows': WindowGuiFactory,
        'Linux': LinuxGuiFactory,
    }
    return factory_dict[system_name]()


if __name__ == '__main__':
    system_name = 'Windows'
    ui = create_factory(system_name)
    app = Application(ui)
    app.create_gui()
