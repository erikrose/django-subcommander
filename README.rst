===================
django-subcommander
===================

Use django-subcommander to write Django management commands that have
subcommands, each optionally having its own distinct options, help, and other
typically per-command behavior. Subcommands are just normal Django
``BaseCommand`` subclasses, so there's very little new to learn. Here's an
example top-level command; you'd put this in your app's
``management.commands.desserts`` module::

    from django_subcommander import SubcommandDispatcher


    class Command(SubcommandDispatcher):
        """The top-level "dessert" command which has several subcommands"""

        help = 'Eat, top, and do various things with desserts.'
        args = '<subcommand> [more arguments and options]'
    
        def _subcommand(self, name):
            """
            Return a management command that implements the subcommand of the
            given name.
            """
            if name == 'eat':
                return EatCommand()
            elif name == 'top':
                ,,,


    class EatCommand(BaseCommand):
        # You could put this in another module or wherever you want.
        help = 'Eat a dessert.'
        args = '[number of bites]'
        
        # Add options here with make_option(), in the usual way.
        
        def handle(self, *args, **options):
            ...

To invoke the subcommand for eating a dessert in 5 bites... ::

    ./manage.py dessert eat 5

To see the help for the ``eat`` subcommand... ::

    ./manage.py dessert eat --help

To see the help for the top-level command... ::

    ./manage.py dessert --help

The help for the top-level command will list its subcommands if you implement
``_subcommand_names``::

    class Command(SubcommandDispatcher):
        ...
        
        def _subcommand(self, name):
            ...
        
        def _subcommand_names(self):
            """Return a list of the names of all the subcommands."""
            return ['eat', 'top']

Then, ``./manage.py dessert --help`` will result in something like this::

    Usage: ...
    
    Options:
      ...
    
    Subcommands:
      eat [number of bites]
      top <topping> [more toppings]


Crazy Stuff
===========

* Notice that ``_subcommand()`` returns a command instance, not a class or a
  module path. Not only does this give you the freedom to put your subcommand
  code wherever you wish, but it also means you can generate or parametrize
  subcommands dynamically, at runtime.
* There's no reason you shouldn't be able to have one ``SubcommandDispatcher``
  return another, thereby implementing multi-level subcommands.


Design Notes
============

Django's management command framework is built on ``optparse``, not the more
modern ``argparse``, which supports subcommands natively. It would be quite a
bit of gluing to get ``argparse`` working with Django's management command
infrastructure, so I took the simple road. This lets authors reuse everything
they already know about writing Django management commands. For example, I had
several groups of pre-existing commands I wanted to organize under a handful of
subcommands. This let me avoid having hundreds of individual files under
``management/commands``; it gave me the freedom to locate all that command code
elsewhere and organize it in a more natural way. Turning the commands into
subcommands required no changes to them at all.

django-subcommander is definitely a "worse is better" solution. It's an eminently practical solution to the profusion of files in ``management/commands``. If it had turned out long and complicated, I probably would have rigged Django to support argparse-based commands instead...hmm, what about making a BaseCommand alternative that's argparse-based?


Future Plans
============

* Tests. I'm using it all day now, but I've been testing it only "in situ".
* More flexibility in how to display the list of subcommands when getting
  ``--help`` on the top-level command
* Support for Django's other command superclasses like ``AppCommand`` and
  ``LabelCommand`` (if, in fact, they don't work already and if there's demand)
* I went a short way down the path of giving ``_subcommand()`` access to the
  whole ``argv`` and having it return any args that weren't used to do
  dispatch. This ended up complicating things significantly for unclear
  benefit. If you'd find this useful, please file a bug.


Version History
===============

0.1
    First release.
