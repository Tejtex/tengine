==================================
Welcome to Tengine's Documentation
==================================

Tengine is a lightweight, flexible, and efficient Entity-Component-System (ECS) framework for Python, designed to help you build modular and scalable systems, especially for game development and simulations.

This documentation provides an overview of Tengine's core modules, installation instructions, and usage examples. Navigate through the sections below to learn more.

Contents:
----------
.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   core
   license

Core Modules
============

Tengine's core functionality is organized into several key modules that work together to form the heart of the ECS system. Learn more about each of these modules below.

.. toctree::
   :maxdepth: 2
   :caption: Detailed Core Modules

   core

Other Modules
=============

Tengine's core doesnt include all the modules. It is designed to be extensible, allowing you to add your own modules or use third-party ones. 
But here are the modules included in tengine:

.. toctree::
   :maxdepth: 2
   :caption: Other Modules

   renderer
   common



Installation
============

To install Tengine, use `pip`:

.. code-block:: bash

   pip install tengine

Usage
=====

After installation, you can start using Tengine by importing it into your Python code. Here is a simple example:

.. code-block:: python

   from tengine.core.component import Component
   from tengine.core.system import System
   from tengine.core.world import World

   class Position(Component):
      def __init__(self, x, y):
         self.x = x
         self.y = y
   class Velocity(Component):
      def __init__(self, dx, dy):
         self.dx =dx
         self.dy = dy

   class VelocitySystem(System):
      
      def update(self, entities, world_info):
         
         for entity in entities:
               if entity.has_component(Position) and entity.has_component(Velocity):
                  entity.get_component(Position).x += entity.get_component(Velocity).dx * world_info.dt
                  entity.get_component(Position).y += entity.get_component(Velocity).dy * world_info.dt
   class PrintSystem(System):
      def update(self, entities, world_info):
         for entity in entities:
               if entity.has_component(Position):
                  pos = entity.get_component(Position)
                  print(pos.x, pos.y)

   world = World()
   world.spawn_entity(Velocity(1, 1), Position(0, 0))
   world.add_system(VelocitySystem())
   world.add_system(PrintSystem())
   world.mainloop()

License
=======
Tengine is licensed under the MIT License. See the LICENSE file for more details.
