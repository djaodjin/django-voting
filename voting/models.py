from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.now

from voting.compat import GenericForeignKey
from voting.managers import VoteManager


SCORES = (
    (+1, u'+1'),
    (-1, u'-1'),
)


class Vote(models.Model):
    """
    A vote on an object by a User.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey('content_type', 'object_id')
    vote = models.SmallIntegerField(choices=SCORES)
    time_stamp = models.DateTimeField(editable=False, default=now)

    objects = VoteManager()

    class Meta:
        db_table = 'votes'
        # One vote per user per object
        unique_together = (('user', 'content_type', 'object_id'),)

    def __unicode__(self):
        return u'%s: %s on %s' % (self.user, self.vote, self.object)

    def is_upvote(self):
        return self.vote == 1

    def is_downvote(self):
        return self.vote == -1
