import itertools

class collisionDetector():

    collidingBoxes = []
    allCollisions = []
    oldCollisions = []

    @classmethod
    def detectCollision(cls, x, y, board):

        collisionList = []

        checkedNumber = board[x][y]

        for i in range(9):
            if i == x:
                continue

            if checkedNumber == board[i][y]:
                collisionList.append([i,y])

            elif ([i,y] in cls.allCollisions) and ([i,y] not in collisionList):
                cls.oldCollisions.append([i,y])

            if i == y:
                continue

            if checkedNumber == board[x][i]:
                collisionList.append([x,i])

            elif ([x,i] in cls.allCollisions) and ([x,i] not in collisionList):
                cls.oldCollisions.append([x,i])

        i0 = x - x % 3
        j0 = y - y % 3

        for i in range(i0, i0 + 3):
            for j in range(j0, j0 + 3):
                if [i,j] == [x,y]:
                    continue

                if (checkedNumber == board[i][j]) and ([i,j] not in collisionList):
                    collisionList.append([i,j])

                elif ([i,j] in cls.allCollisions) and ([i,j] not in collisionList):
                    cls.oldCollisions.append([i,j])

        return collisionList



    @classmethod
    def checkCollision(cls, x, y, board):
        cls.collidingBoxes.append([x,y])

        collisions = []
        tmpList = []
        for box in cls.collidingBoxes:
            cx, cy = box
            tmpList = cls.detectCollision(cx, cy, board)

            if not tmpList:
                if box in cls.collidingBoxes:
                    cls.collidingBoxes.remove(box)

            else:
                collisions.extend(tmpList)
                collisions.append(box)

        collisions.sort()
        return list(collisions for collisions,_ in itertools.groupby(collisions))



    @classmethod
    def markCollision(cls, x, y, board, button):
        collisionList = cls.checkCollision(x, y, board)

        for collision in collisionList:
            cx, cy = collision
            button[cx][cy].configure(fg = "#ff0000")
            cls.allCollisions.append(collision)

        for old in cls.oldCollisions:
            cx, cy = old
            button[cx][cy].configure(fg = "#7aa719")
            cls.allCollisions.remove(old)

            if old in cls.collidingBoxes:
                cls.collidingBoxes.remove(old)

        cls.oldCollisions.clear()
