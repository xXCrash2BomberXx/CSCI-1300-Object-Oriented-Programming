class World(object):
    '''
    The goal of this assignment is to create and implement a new class named World, which provides a basic model for a simple one-player game. The world is a two-dimensional space, organized in rows and columns, containing a single player who can move in any of four directions, so long as the player remains within the bounds of the world.
    '''

    def __init__(self, rows: int, columns: int, pStart: tuple = (0, 0)) -> None:
        '''
        The constructor should accept two parameters

        Parameters
        ----------
        rows : +int
            number of rows.
        columns : +int
            number of columns.
        pStart : tuple, optional
            The player should initially be located at the bottom-left corner within the world, which we will canonically define as row 0 and column 0
        '''
        self._Rows = rows  # Height
        self._Columns = columns  # Width
        self._player = pStart
        self._obstacles = []

    def playerLocation(self) -> tuple:
        '''
        For example, the initial position for the player is denoted as (0,0).

        Returns
        -------
        tuple
            Returns a (row, column) tuple that identifies the current location of the player.
        '''
        return super(World, self).__getattribute__("_player")

    def numRows(self) -> int:
        '''
        Returns
        -------
        int
            Returns the number of rows within the world.
        '''
        return super(World, self).__getattribute__("_Rows")

    def numColumns(self) -> int:
        '''
        Returns
        -------
        int
            Returns the number of columns within the world.
        '''
        return super(World, self).__getattribute__("_Columns")

    def moveUp(self) -> bool:
        '''
        Moves the player up one row, so long as that remains a legal position within the world. Otherwise, the player's position should be unchanged.

        Returns
        -------
        bool
            The method should return True if the movement was allowed, and False otherwise.
        '''
        return self.moveTo(self.playerLocation()[0]+1, self.playerLocation()[1])

    def moveDown(self) -> bool:
        '''
        Moves the player down one row, so long as that remains a legal position within the world. Otherwise, the player's position should be unchanged.

        Returns
        -------
        bool
            The method should return True if the movement was allowed, and False otherwise.
        '''
        return self.moveTo(self.playerLocation()[0]-1, self.playerLocation()[1])

    def moveLeft(self) -> bool:
        '''
        Moves the player to the left by one column, so long as that remains a legal position within the world. Otherwise, the player's position should be unchanged.

        Returns
        -------
        bool
            The method should return True if the movement was allowed, and False otherwise.
        '''
        return self.moveTo(self.playerLocation()[0], self.playerLocation()[1]-1)

    def moveRight(self) -> bool:
        '''
        Moves the player to the right by one column, so long as that remains a legal position within the world. Otherwise, the player's position should be unchanged.

        Returns
        -------
        bool
            The method should return True if the movement was allowed, and False otherwise.
        '''
        return self.moveTo(self.playerLocation()[0], self.playerLocation()[1]+1)

    def moveTo(self, newRow: int, newColumn: int) -> bool:
        '''
        Moves the player directly to the given row and column, so long as that is a legal position in the world. Otherwise the player's position should be unchanged.

        Parameters
        ----------
        newRow : int
            X-Coordinate to move the Player to.
        newColumn : int
            Y-Coordinate to move the Player to.

        Returns
        -------
        bool
            The method should return True if the movement was allowed, and False otherwise.

        '''
        if newRow in range(self.numRows()) and newColumn in range(self.numColumns()) and (newRow, newColumn) not in self.getObstacles():
            super(World, self).__setattr__("_player", (newRow, newColumn))
            return True
        else:
            return False

    def addObstacle(self, row: int, column: int) -> bool:
        '''
        Add an obstacle to the world at the given row and column.

        Parameters
        ----------
        row : int
            Y-Coordinate to place the Obstacle at.
        column : int
            X-Coordinate to place the Obstacle at.

        Returns
        -------
        bool
            The method should return True if the placement was allowed, and False otherwise.

        '''
        if row in range(self.numRows()) and column in range(self.numColumns()) and (row, column) not in self.getObstacles() and (row, column) != self.playerLocation():
            super(World, self).__getattribute__("_obstacles").append((row, column))
            return True
        else:
            return False

    def getObstacles(self) -> list:
        '''
        We rely on this for rendering your world.

        Returns
        -------
        list
            Return a list of all obstacles currently in the world.
        '''
        return super(World, self).__getattribute__("_obstacles")

    def __repr__(self, pl: str = "O", ob: str = "X", el: str = "_", sp: str = " ") -> str:  # Output as a 2D map
        return "\n".join([
            sp.join([
                pl if (x, y) == self.playerLocation()
                else
                ob if (x, y) in self.getObstacles()
                else
                el
                for y in range(self.numColumns())])  # x
            for x in range(self.numRows())])  # y

    def __setattr__(self, name: str, value) -> None:  # Prevent modifying constants and private attributes
        try:
            super(World, self).__getattribute__(name)
            t = True
        except AttributeError:
            t = False
        if name[0] == "_" and t:
            raise PermissionError("Cannot Change Private Variable " + name)
        elif name[0].isupper() and t:
            raise PermissionError("Cannot Change Constant " + name)
        else:
            super(World, self).__setattr__(name, value)

    def __getattribute__(self, name: str):  # Prevent access to private attributes
        if name[0] == "_" and ((name[1] != "_") if len(name) > 1 else True):
            raise PermissionError("Cannot Access Private Attribute " + name)
        else:
            return super(World, self).__getattribute__(name)
