
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete

@receiver(post_init, sender Campaign, dispatch_uid="campaign_signal")
def campaign_signal(sender, **kwargs):
    instance  = kwargs.get('instance')
    print('Campaign created')


@receiver(post_save, sender Campaign, dispatch_uid="campaign_signal")
def campaign_signal(sender, **kwargs):
    instance  = kwargs.get('instance')
    print('Campaign updated')

@receiver(post_delete, sender Campaign, dispatch_uid="campaign_signal")
def campaign_signal(sender, **kwargs):
    instance  = kwargs.get('instance')
    print('Campaign deleted')








    
