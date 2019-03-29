
import datetime
import random
import uuid

from django.conf import settings
from django.db import models
from django.forms import fields

from proj.apps.chess.models.managers import ChessSnapshotManager
from proj.apps.chess.models.querysets import ChessSnapshotQuerySet


class ChessSnapshot(models.Model):

    objects = ChessSnapshotManager.from_queryset(ChessSnapshotQuerySet)()

    # - - - - - - - -
    # config actions
    # - - - - - - - -

    ACTION_JOIN_MATCH = 'join_match'

    ACTION_CLOSE_MATCH = 'close_match'
    ACTION_RESIGN = 'resign'

    ACTION_TAKE_MOVE = 'take_move'
    ACTION_UNDO_MOVE = 'undo_move'
    ACTION_SUGGEST_MOVE = 'suggest_move'

    ACTION_ASK_UNDO_REQUEST = 'ask_undo_request'
    ACTION_APPROVE_UNDO_REQUEST = 'approve_undo_request'
    ACTION_REJECT_UNDO_REQUEST = 'reject_undo_request'

    ACTION_CHOICES = (
        ACTION_JOIN_MATCH,
        ACTION_CLOSE_MATCH,
        ACTION_RESIGN,
        ACTION_DECLINE_REMATCH,
        ACTION_TAKE_MOVE,
        ACTION_SUGGEST_MOVE,
        ACTION_ASK_UNDO_REQUEST,
        ACTION_APPROVE_UNDO_REQUEST,
        ACTION_REJECT_UNDO_REQUEST,
        ACTION_UNDO_MOVE,
    )

    # - - - - - -
    # properties
    # - - - - - -

    created_at = models.DateTimeField(
        default=datetime.datetime.now
    )

    # TODO add the color of who did the action
    action = models.CharField()
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='actors',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    board = models.CharField(
        max_length=92,
    )

    game = models.ForeignKey(
        'chess.ChessGame',
        related_name='snapshots',
        on_delete=models.DO_NOTHING,
    )

    step = models.IntegerField()

    # - - - - -
    # methods
    # - - - - -

    def create(self, *args, **kwargs):
        '''
        Override default create method.
        '''
        from .models import ChessGame

        code = kwargs.pop('code', False)
        if code:
            raise ValueError('ChessGame.code must be randomly generated.')

        # randomly generate a code
        while True:
            code = self.generate_code()
            if ChessGame.objects.active().filter(code=code).exists():
                continue
            break

        kwargs['code'] = code
        return super.create(*args, **kwargs)
