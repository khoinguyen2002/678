game_objects = []

def add(game_object):
    game_objects.append(game_object)

def update():
    for game_object in game_objects:
        if game_object.is_active:
            game_object.update()

def render(canvas):
    for game_object in game_objects:
        if game_object.is_active:
            game_object.render(canvas)

def recycle(t, x, y):
    for game_object in game_objects:
        if not game_object.is_active and type(game_object) == t:
            game_object.is_active = True
            game_object.x = x
            game_object.y = y
            return game_object

    new_game_object = t(x, y)
    add(new_game_object)
    return new_game_object

def collide_with(box_collider):
    collie_list = []
    for game_object in game_objects:
        if game_object.is_active and game_object.box_collider is not None:
            if game_object.box_collider.overlap(box_collider):
                collie_list.append(game_object)
    return collie_list


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.is_active = True
        self.box_collider = None

    def update(self):
        if self.box_collider is not None :
            self.box_collider.x = self.x
            self.box_collider.y = self.y

    def render(self, canvas):
        if self.image is not None:
            width = self.image.get_width()
            height = self.image.get_height()
            render_pos = (self.x - width / 2, self.y - height / 2)
            canvas.blit(self.image, render_pos)
        if self.box_collider is not None:
            # self.box_collider.render(canvas)
            pass


    def deactivate(self):
        self.is_active = False