from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    disabled = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)

    @property
    def datetime(self):
    	return self.created_datetime.strftime('%b %d %Y')

    def __str__(self):
    	if self.disabled:
    		return '[%s] %s (disabled)' % (self.title, self.created_datetime.strftime('%b %d %Y'))
    	else:
    		return '[%s] %s' % (self.title, self.datetime)