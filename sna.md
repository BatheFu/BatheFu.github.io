---
layout: default
---


# My Current Working Projects

For the last ten months, I was still movitived by the big picture of analytical sociology, focus on a set of toolkit including social network analysis and agent-based modeling, as to establish links between the micro world and the macro world. To some extent, it is the descendant of R.Merton who regards the world as an evolving system, and sociologists are those who discover the secrets of it based on their current social contexts. Fortunenately, I have found a primitive information source to research on -- the medical forum DingXiangYuan(DXY). This is a professional website for doctors, researchers, and medical students to share their knowledge, as well as to develop a supportive community in their life and work.  I hope that this research could reveal the patterns of their interactions, and whether they comform to the characteristics of non-scale networks given that all the communications are under a framework where ranks and departments might affect people's choices, activities, and trust.

Click [here](http://bbs.dxy.cn) to visit the forum's homepage.

With the help of a friend for the purpose of data collecting by scraping the pages of the members discussion, we analyzed the interaction patterns since 2002(the website's initial year) using social network analysis. I've summarised a few aspects of our findings(mostly explorable ones) as follows to make it easy for you to approach.

## Structure and Roles

Here shows the basic structure of the whole network from the randomly chosed 18000 data points. Each point has its function in the graph, which we call roles, mainly to convey information, to lead the conversation, to support others' opinion, etc. Also we colored and sized them due to their ranks and labels. (see details in the pdf) Actually rank has influencial impact on the size of the cluster, while which department you belong to doesn't means a lot. You could guess that the graph would conform to the power law from the graph, too.

{% include image.html url="/images/structrue.png" description="Left: Labeled with department, Right: Labeled with rank. The gate keeper in the middle belongs to an account run by the forum itself, if removed, the graph would be rather mixed up." %}

## Lifespan

Here is one image that smoothens the life span of the users, from which you could have a glance at when would people stay, and when would they leave.

{% include image.html url="/images/sur.png" description="Survival analysis: x-axis represents the active years of a member(the last speaking time mimus the first one), y-axis represents the probablity of suvival(Will they continue to be active give x years)" %}

As we see in the picture, most members are active for less than one year, while some of them could keep active with the development of the forum. They are key members in the forum who knows the history of this community, not only serve as the information distributors, but also administrators, and gate keepers to lead more people engage in discussions. These leaders do not take the role of all above all the time, therefore, it's crucial to find out how these alternations of leaders happen as the time goes on, and how does it relates to the rigor of  the forum.

## Limitations

This project has inevitable drawbacks for multiple reasons. First, though the archive of the communications are complete, we could not reach to those people who jump into the discussions by search engine. They might then contribute to the discussion but then never logged in again. That's why we have so many one-degree points. These points were finally discarded in the analysis. Second, the alternation of the leaders have both reasons from the regulation of the forum and individual factors, before inplementing real interviews with those leaders, we still have quite vague inpressions on this phenomena. 

However, I'm stuck in further research into these personal experiences to find why the leaders rotated as we seen in the graph, because we cannot get direct contact with these members. In December, I sent requests to some of the leaders but receive no repsponses, partly because they are busy, and they need the researchers to have an official position to carry on this sort of interview that has risk of exposing them to the publication side. So we are looking for some other quantitative methods as to move on. If you would like to see what we have done for more details, please **DOWNLOAD THE PDF** [here](./main.pdf) and offer us some advice on it.