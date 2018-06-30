from django.conf.urls import patterns,url
from goal.views import worldcup_team
from goal.views import worldcup_goal
from goal.views import worldcup_gap
from goal.views import wordcup_promotion

urlpatterns=patterns(
    '',
    url(r'^teamname/$',worldcup_team,name='worldcup_team'),
    url(r'^teamgoal/$',worldcup_goal,name='worldcup_goal'),
    url(r'^teamgap/$',worldcup_gap,name='worldcup_gap'),
    url(r'^teampromotion/$',wordcup_promotion,name='worldcup_promotion'),
)