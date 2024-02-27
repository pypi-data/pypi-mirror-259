from __future__ import annotations
from typing import Type
import scpup
import pygame
from scpup._internal import load_image as _load_image


__all__: list[str] = [
  "EauView",
]


class EauViewMeta(type):
  """Metaclass for EauView class. Implements a Singleton so that only 1 instance
  exists of all subclasses. For example if you have class View1 and class View2
  and you create an instance of class View1, and then create an instance of
  View2, the instance of View1 will get deleted before the instance of View2
  gets created."""
  _instance: EauView | None = None
  _views_: dict[str, Type[EauView]] = {}

  def __call__(cls, *args, **kwargs):
    if cls._instance is not None:
      cls._instance.sprites.empty()
      del cls._instance
    cls._instance = super().__call__(*args, **kwargs)
    return cls._instance

  def get(cls, view_name: str) -> Type[EauView] | None:
    return cls._views_.get(view_name, None)


class EauView(metaclass=EauViewMeta):
  """A game view.

  Attributes:
    sprites:
      The sprite group that has the sprites that belong to the view.
    texts:
      The text group that has the texts that belong to the view.
  """
  __slots__: tuple = (
    "sprites",
    "texts"
  )

  @classmethod
  def __init_subclass__(cls, /, *, bgpath: str | None = None, player_sprite: str, **kwargs):
    """Subclass customization so that subclasses can specify their background
    image when subclassing and the sprite that players will use when this view
    is created. For example:

    ```python
    class View1(EauView, 'path', 'to', 'image.png', player_sprite="Sprite"):
      ...
    ```

    Args:
      *bgpaths:
        Path segments of the background image of the subclass. It has to be
        under `<root>/assets/images/`.
      player_sprite:
        The name of the class of the sprite that will be set to players when
        creating an instance of the subclass. It can also be the class itself,
        because in case the sprite is not imported elsewhere then it will not be
        found if only the name is specified.
    """
    super().__init_subclass__(**kwargs)
    cls.background = _load_image(bgpath)[0] if bgpath else None
    cls._views_[cls.__name__] = cls
    cls.player_sprite = player_sprite

  @classmethod
  def initial_position(cls, pid: str) -> scpup.EauPosition:
    return scpup.EauPosition(0, 0)

  def __init__(self):
    """Initialize a view

    When subclassing, don't forget to call `super().__init__()` because it
    does initialization logic that is needed for the view to work correctly.
    """
    self.sprites = self.init_sprites()
    self.texts = self.init_texts()

  def init_texts(self) -> scpup.EauTextsGroup:
    """Initialize the texts that are part of this view

    When subclassing EauView, if the subclass must display text then this method
    should return an EauTextGroup with the texts that will be shown. This method
    is not abstract because there might be views that don't have texts, so not
    all view need to implement this method

    Returns:
      The text group with the texts that belong to this view
    """
    return scpup.EauTextsGroup()

  def init_sprites(self) -> scpup.EauGroup:
    """Initialize the sprites that are part of this view

    When subclassing EauView, all the sprites that are specifically part of this
    view should be added to an EauGroup and returned from this method.

    Returns:
      The sprite group with the sprites that belong to this view
    """
    return scpup.EauGroup()

  def draw(self, surface: pygame.Surface) -> None:
    """Draw this view's sprites to a surface

    Args:
      surface:
        The target surface
    """
    self.texts.draw(surface)
    self.sprites.draw(surface)
    scpup.EauPlayer.draw(surface)

  def clear(self, surface: pygame.Surface, background: pygame.Surface) -> None:
    """Clear this view's sprites from a surface with a background surface

    Args:
      surface:
        The target surface
      background:
        The background surface
    """
    self.sprites.clear(surface, background)
    scpup.EauPlayer.clear(surface, background)

  def update(self, *args, skip_player=False, **kwargs) -> None:
    """Update this view's sprites"""
    self.sprites.update(*args, **kwargs)
    if not skip_player:
      scpup.EauPlayer.update(*args, **kwargs)

  def on(self, *, event_name: str, actioner: scpup.EauSprite, **_) -> None:
    """Listener to events. This will get triggered automatically whenever an
    event for the view is received by the EauEventService.

    Args:
      event_name: The name of the event
      actioner: The sprite that triggered the event
    """
    for spr in self.sprites:
      if event_name == "back":
        if backbtn := next((spr for spr in self.sprites if isinstance(spr, scpup.EauBackButton)), None):
          backbtn.action()
      elif scpup.eaucollidesprite(spr, actioner):
        if isinstance(spr, scpup.EauAnimatedSprite):
          spr.trigger(event_name)
        if event_name == "click" and isinstance(spr, scpup.EauButton):
          spr.action()
