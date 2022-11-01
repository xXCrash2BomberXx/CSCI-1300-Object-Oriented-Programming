from world import World


class Oasis(World):
    def __init__(self, rows: int, columns: int) -> None:
        '''
        Initialize Oasis

        Parameters
        ----------
        rows : int
            rows in the map.
        columns : int
            columns in the map.

        '''
        ret = super().__init__(rows, columns)
        self._Eggs = set()
        self._score = 0
        return ret

    def moveTo(self, row: int, column: int) -> bool:
        '''
        Move to row and column in map

        Parameters
        ----------
        row : int
            row to move to.
        column : int
            column to move to.

        Returns
        -------
        bool
            Whether or not the player moved.

        '''
        ret = super().moveTo(row, column)
        if (row, column) in self._Eggs:
            self._Eggs.remove((row, column))
            self._score += 1
        return ret

    def addEgg(self, row: int, column: int) -> None:
        '''
        Add an egg to the map

        Parameters
        ----------
        row : int
            row to place the egg in.
        column : int
            column to place the egg in.

        '''
        return self._Eggs.add((row, column))

    def eggLocations(self) -> set:
        '''
        Get the set of eggs in the map

        Returns
        -------
        set
            eggs in the map.

        '''
        return self._Eggs

    def getScore(self) -> int:
        '''
        Get the score of eggs collected

        Returns
        -------
        int
            score of eggs collected.

        '''
        return self._score
