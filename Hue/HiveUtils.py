import pyhs2
import datetime
class HiveClient:
    def __init__(self, db_host, user, password, database, port=10000, authMechanism="PLAIN"):
        """
        create connection to hive server2
        """
        self.conn = pyhs2.connect(host=db_host,
                                  port=port,
                                  authMechanism=authMechanism,
                                  user=user,
                                  password=password,
                                  database=database,
                                  )

    def query(self, sql):

        """
        query
        """

        with self.conn.cursor() as cursor:

            cursor.execute(sql)

            return cursor.fetch()

    def action(self, sql):

        """
        query
        """

        with self.conn.cursor() as cursor:

            cursor.execute(sql)

            return cursor

    def close(self):

        """
        close connection
        """
        self.conn.close()


if __name__ == '__main__':
    hive_client = HiveClient(db_host='59.111.7.43', port=10000, user='hdfs', password='mypass',

                             database='default', authMechanism='PLAIN')

#     d = datetime.datetime.strptime('2018-03-23', '%Y-%m-%d')
#     for t in range(0,62):
#         date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#         sql = '''
#                     Insert overwrite table qn_guanning.guanningpersonal
#     partition (ds='%s')
#     select a.server,a.id,concat_ws(',',a.seq,if(b.role_id is null,'0,0,0,0,0,0,0,0,0,0',b.seq)
#     ,if(c.role_id is null,'0,0,0,0,0,0,0,0,0,0,0,0,0',c.seq))
#     from  (select min(server) as server,id,
#                 concat_ws(',',cast(round(avg(iswin),2) as string),cast(round(avg(xiulian),2) as string)
#                                 ,cast(round(avg(total_score),2) as string),cast(round(avg(help_num),2) as string)
#                                 ,cast(round(avg(kill_score),2) as string),cast(round(avg(flag_score),2) as string)
#                                 ,cast(round(avg(xiuwei),2) as string),cast(round(avg(equip_score),2) as string)
#                                 ,cast(round(avg(team_score),2) as string),cast(round(avg(killed_score),2) as string)
#                                 ,cast(round(avg(score_count),2) as string),cast(round(avg(grade),2) as string)
#                                 ,cast(round(min(class),2) as string),cast(round(count(*),2) as string)) as seq
#             from qndb.h_guanning_result where ds>='%s' and ds<='%s' group by id)a
#     left outer join
#     (select
#             role_id,
#                 concat_ws(',',cast(round(max(maxhp),2) as string),cast(round(max(pdef),2) as string)
#                                 ,cast(round(max(mdef),2) as string),cast(round(max(pmiss),2) as string)
#                                 ,cast(round(max(mmiss),2) as string),cast(round(max(phit),2) as string)
#                                 ,cast(round(max(mhit),2) as string),cast(round(max(pfatal),2) as string)
#                                 ,cast(round(max(mfatal),2) as string),cast(round(max(pdef),2) as string)) as seq
#             from qndb.h_guanning_roleinfo1 where ds>='%s' and ds<='%s' group by role_id)b
#     on a.id=b.role_id
#     left outer join
#     (select
#             role_id,
#                 concat_ws(',',cast(round(max(block),2) as string),cast(round(max(ignoreblock),2) as string)
#                                 ,cast(round(max(enhancedizzy),2) as string),cast(round(max(enhancemass),2) as string)
#                                 ,cast(round(max(enhancesilence),2) as string),cast(round(max(antidizzy),2) as string)
#                                 ,cast(round(max(antimass),2) as string),cast(round(max(antisilence),2) as string)
#                                 ,cast(round(max(antiingorewater),2) as string),cast(round(max(antiingoreice),2) as string)
#                                 ,cast(round(max(antiingorefire),2) as string),cast(round(max(antiingorethunder),2) as string)
#                                 ,cast(round(max(xiuwei),2) as string)) as seq
#     from qndb.h_guanning_roleinfo2 where ds>='%s' and ds<='%s' group by role_id)c
#     on a.id=c.role_id
#                   '''%((d+datetime.timedelta(7+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'))
#         result = hive_client.action(sql)
#         print t
#
#
#     d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
#     for t in range(0,61):
#         date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#         sql = '''
#                           Insert overwrite table qn_guanning.guanningpersonal_one partition (ds='%s')
#     select a.server,a.id,a.iid,concat_ws(',',a.seq,if(b.role_id is null,concat(repeat('0,',9),'0'),b.seq)
#     ,if(c.role_id is null,concat(repeat('0,',12),'0'),c.seq))
#     from  (select min(server) as server,id,iid,
#                                  concat_ws(',',cast(round(avg(xiulian),2) as string)
#     ,cast(round(avg(total_score),2) as string),cast(round(avg(help_num),2) as string)
#     ,cast(round(avg(kill_score),2) as string),cast(round(avg(flag_score),2) as string)
#     ,cast(round(avg(xiuwei),2) as string),cast(round(avg(equip_score),2) as string)
#     ,cast(round(avg(team_score),2) as string),cast(round(avg(killed_score),2) as string)
#     ,cast(round(avg(score_count),2) as string),cast(round(avg(grade),2) as string)
#     ,cast(round(min(class),2) as string),cast(round(count(*),2) as string)) as seq
#     from qndb.h_guanning_result where  ds='%s' group by id,iid)a
#     left outer join
#     (select
#     role_id,scene_id,
#     concat_ws(',',cast(round(max(maxhp),2) as string),cast(round(max(pdef),2) as string)
#     ,cast(round(max(mdef),2) as string),cast(round(max(pmiss),2) as string)
#     ,cast(round(max(mmiss),2) as string),cast(round(max(phit),2) as string)
#     ,cast(round(max(mhit),2) as string),cast(round(max(pfatal),2) as string)
#     ,cast(round(max(mfatal),2) as string),cast(round(max(pdef),2) as string)) as seq
#     from qndb.h_guanning_roleinfo1 where ds='%s' group by role_id,scene_id)b
#     on a.id=b.role_id and a.iid=b.scene_id
#     left outer join
#     (select
#     role_id,scene_id,
#     concat_ws(',',cast(round(max(block),2) as string),cast(round(max(ignoreblock),2) as string)
#     ,cast(round(max(enhancedizzy),2) as string),cast(round(max(enhancemass),2) as string)
#     ,cast(round(max(enhancesilence),2) as string),cast(round(max(antidizzy),2) as string)
#     ,cast(round(max(antimass),2) as string),cast(round(max(antisilence),2) as string)
#     ,cast(round(max(antiingorewater),2) as string),cast(round(max(antiingoreice),2) as string)
#     ,cast(round(max(antiingorefire),2) as string),cast(round(max(antiingorethunder),2) as string)
#     ,cast(round(max(xiuwei),2) as string)) as seq
#     from qndb.h_guanning_roleinfo2 where ds='%s' group by role_id,scene_id)c
#     on a.id=c.role_id and a.iid=c.scene_id
#
#                           '''%(date,date,date,date)
#         result = hive_client.action(sql)
#         print t
# #
# #
#     d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
#     for t in range(0,60):
#         date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#         sql = '''
#                     Insert overwrite table qn_guanning.guanninggamewithfeature
#                     partition (ds='%s')
#
#                     select min(time),server,iid
#                     ,concat_ws(';',collect_set(if(iswin>0,features,NULL))) as win_features
#                     ,concat_ws(';',collect_set(if(iswin<0,features,NULL))) as lose_features
#                     from (
#                     select a.time,a.server,a.iid,a.id,if(b.features is null,concat(repeat('0,',36),'0'),b.features) as features,iswin
#                     from
#                     (
#                     SELECT time,server,iid,id,iswin
#                     from qndb.h_guanning_result
#                     where ds='%s'
#                     )a
#
#                     left outer join
#                     (select role_id,features from qn_guanning.guanningpersonal where ds='%s')b
#                     on a.id=b.role_id
#                     )c
#                     group by server,iid
#                   '''%(date,date,date)
#         result = hive_client.action(sql)
#         print t
# #
# #
# #
#
#     d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
#     for t in range(0,60):
#         date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#         sql = '''
#                     Insert overwrite table qn_guanning.guanninggamewithfeature_one
# partition (ds='%s')
#
# select min(time),server,iid
# ,concat_ws(';',collect_set(if(iswin>0,features,NULL))) as win_features
# ,concat_ws(';',collect_set(if(iswin<0,features,NULL))) as lose_features
# from (
# select a.time,a.server,a.iid,a.id,if(b.features is null
# ,concat(repeat('0,',35),'0')
# ,b.features) as features,iswin
# from
# (
# SELECT time,server,iid,id,iswin
# from qndb.h_guanning_result
# where ds='%s'
# )a
#
# left outer join
# (select role_id,iid,features from qn_guanning.guanningpersonal_one where ds='%s')b
# on a.id=b.role_id and a.iid=b.iid
# )c
# group by server,iid
#                   '''%(date,date,date)
#         result = hive_client.action(sql)
#         print t
    d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
    for t in range(0,1):
        date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
        sql='''ADD JAR /opt/cloudera/parcels/CDH-5.13.0-1.cdh5.13.0.p0.29/jars/hive-hcatalog-core-1.1.0-cdh5.13.0.jar;'''
        result = hive_client.action(sql)
        sql = '''
      select * from(
select front.server,front.id, front.mean,front.xiuwei,front.xiulian,front.equip_score, behind.sum_ability from(
select * from (
select fff.server, fff.id, fff.mean, ffff.xiuwei, ffff.xiulian,ffff.equip_score from(
select * from (
select server,id,mean,rank() over(partition by f.server,f.id order by f.rank desc)rank_id from(
select bbb.server,aaa.id,aaa.mean, 1 as rank from(
select * from(
SELECT id,avg(total_score) AS mean FROM (
SELECT server,time,id,total_score,rank() OVER ( PARTITION BY a.server,a.id ORDER BY a.time) AS temp from (
SELECT server,time,id,total_score FROM qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 60 AND grade<=69 ORDER BY id,time) AS a) 
AS b GROUP BY b.id)as aa)aaa
join(
select server,id from(
select server,id,time,rank()over(partition by a2.id order by time desc)as time_rank from(
select server,time,id from qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 60 AND grade<=69)as a2 order by id,server)as b2 where time_rank=1)bbb on (bbb.id = aaa.id)
union all
select bbb.server,aaa.id,aaa.mean, 2 as rank from(
select * from(
SELECT id,avg(total_score) AS mean FROM (
SELECT server,time,id,total_score,rank() OVER ( PARTITION BY a.server,a.id ORDER BY a.time) AS temp from (
SELECT server,time,id,total_score FROM qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 70 AND grade<=89 ORDER BY id,time) AS a) 
AS b GROUP BY b.id)as aa)aaa
join(
select server,id from(
select server,id,time,rank()over(partition by a2.id order by time desc)as time_rank from(
select server,time,id from qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 70 AND grade<=89)as a2 order by id,server)as b2 where time_rank=1)bbb on (bbb.id = aaa.id)
union all
select bbb.server,aaa.id,aaa.mean, 3 as rank from(
select * from(
SELECT id,avg(total_score) AS mean FROM (
SELECT server,time,id,total_score,rank() OVER ( PARTITION BY a.server,a.id ORDER BY a.time) AS temp from (
SELECT server,time,id,total_score FROM qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 90 AND grade<=109 ORDER BY id,time) AS a) 
AS b GROUP BY b.id)as aa)aaa
join(
select server,id from(
select server,id,time,rank()over(partition by a2.id order by time desc)as time_rank from(
select server,time,id from qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 90 AND grade<=109)as a2 order by id,server)as b2 where time_rank=1)bbb on (bbb.id = aaa.id)
union all
select bbb.server,aaa.id,aaa.mean, 4 as rank from(
select * from(
SELECT id,avg(total_score) AS mean FROM (
SELECT server,time,id,total_score,rank() OVER ( PARTITION BY a.server,a.id ORDER BY a.time) AS temp from (
SELECT server,time,id,total_score FROM qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00' and grade >= 110 AND grade<=129  ORDER BY id,time) AS a) 
AS b GROUP BY b.id)as aa)aaa
join(
select server,id from(
select server,id,time,rank()over(partition by a2.id order by time desc)as time_rank from(
select server,time,id from qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00' and grade >= 110 AND grade<=129 )as a2 order by id,server)as b2 where time_rank=1)bbb on (bbb.id = aaa.id)
union all
select bbb.server,aaa.id,aaa.mean, 5 as rank from(
select * from(
SELECT id,avg(total_score) AS mean FROM (
SELECT server,time,id,total_score,rank() OVER ( PARTITION BY a.server,a.id ORDER BY a.time) AS temp from (
SELECT server,time,id,total_score FROM qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 130 AND grade<=150 ORDER BY id,time) AS a) 
AS b GROUP BY b.id)as aa)aaa
join(
select server,id from(
select server,id,time,rank()over(partition by a2.id order by time desc)as time_rank from(
select server,time,id from qndb.h_guanning_result WHERE time > '2018-04-22 00:00:00'and grade >= 130 AND grade<=150)as a2 order by id,server)as b2 where time_rank=1)bbb on (bbb.id = aaa.id)) as f order by id, server)as fina where rank_id = 1) fff
join(
select * from(
select id, xiuwei,xiulian,equip_score,rank() over (partition by a.id order by a.time desc) as rank_time from( 
SELECT time,id,xiuwei,xiulian,equip_score from qndb.h_guanning_result where time > '2018-04-22') as a) as b where rank_time = 1)ffff on (fff.id = ffff.id)) as l)front
left join(
select * from(
select a.sum_ability, a.role_id from(
select ability.sum_ability,ability.role_id, row_number() over (partition by ability.role_id order by ability.ds desc) as time_rank from(
select advanced_skill+banghuifabao+banghuijineng+banghuikangxing+base_reforce+chenghao+chuanjiabao+chuzhanlingshou+equip_skill+fangwunengli+futilingshou
+other_attributes+qianshi+shenbing+shimenmiji+shizhiling+wenshi+xiuchi+xiulian+xiushen+xiuwei+xiuxing+zaoshenlifo as sum_ability, role_id, ds
from qn_src.h_player_capability_new where ds >'2018-05-11' order by role_id)as ability)as a where time_rank =1)as asdf)behind on (behind.role_id = front.id))as fina_gn
                      '''
        result = hive_client.query(sql)
        print t
        f=open('lihaoV2.txt','a+')
        f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
        f.write('\n')
        f.close()
    hive_client.close()





# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,60):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                     Insert overwrite table qn_guanning.guanninggame
#                     partition (ds='%s')
#                     SELECT min(time),server,iid,concat_ws(',',collect_set(concat_ws(':',cast(id as STRING),cast(iswin as String))))
#                     from qndb.h_guanning_result
#                     where ds='%s'
#                     group by server,iid
#                   '''%(date,date)
#     result = hive_client.action(sql)

# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,60):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                 Insert overwrite table qn_guanning.guanningpersonal
# partition (ds='%s')
# select a.server,a.id,concat_ws(',',a.seq,if(b.role_id is null,'0,0,0,0,0,0,0,0,0,0,0,0',b.seq)
# ,if(c.role_id is null,'0,0,0,0,0,0,0,0,0,0,0,0,0',c.seq))
# from  (select min(server) as server,id,
#             concat_ws(',',cast(round(avg(iswin),2) as string),cast(round(avg(xiulian),2) as string)
#                             ,cast(round(avg(total_score),2) as string),cast(round(avg(help_num),2) as string)
#                             ,cast(round(avg(kill_score),2) as string),cast(round(avg(flag_score),2) as string)
#                             ,cast(round(avg(xiuwei),2) as string),cast(round(avg(equip_score),2) as string)
#                             ,cast(round(avg(team_score),2) as string),cast(round(avg(killed_score),2) as string)
#                             ,cast(round(avg(score_count),2) as string),cast(round(avg(grade),2) as string)
#                             ,cast(round(min(class),2) as string),cast(round(count(*),2) as string)) as seq
#         from qndb.h_guanning_result where ds>='%s' and ds<='%s' group by id)a
# left outer join
# (select
#         role_id,
#             concat_ws(',',cast(round(max(maxhp),2) as string),cast(round(max(patt),2) as string)
#                             ,cast(round(max(matt),2) as string),cast(round(max(pdef),2) as string)
#                             ,cast(round(max(mdef),2) as string),cast(round(max(pmiss),2) as string)
#                             ,cast(round(max(mmiss),2) as string),cast(round(max(phit),2) as string)
#                             ,cast(round(max(mhit),2) as string),cast(round(max(pfatal),2) as string)
#                             ,cast(round(max(mfatal),2) as string),cast(round(max(pdef),2) as string)) as seq
#         from qndb.h_guanning_roleinfo1 where ds>='%s' and ds<='%s' group by role_id)b
# on a.id=b.role_id
# left outer join
# (select
#         role_id,
#             concat_ws(',',cast(round(max(block),2) as string),cast(round(max(ignoreblock),2) as string)
#                             ,cast(round(max(enhancedizzy),2) as string),cast(round(max(enhancemass),2) as string)
#                             ,cast(round(max(enhancesilence),2) as string),cast(round(max(antidizzy),2) as string)
#                             ,cast(round(max(antimass),2) as string),cast(round(max(antisilence),2) as string)
#                             ,cast(round(max(antiingorewater),2) as string),cast(round(max(antiingoreice),2) as string)
#                             ,cast(round(max(antiingorefire),2) as string),cast(round(max(antiingorethunder),2) as string)
#                             ,cast(round(max(xiuwei),2) as string)) as seq
# from qndb.h_guanning_roleinfo2 where ds>='%s' and ds<='%s' group by role_id)c
# on a.id=c.role_id
#               '''%((d+datetime.timedelta(7+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'),date,(d+datetime.timedelta(6+t)).strftime('%Y-%m-%d'))
#     result = hive_client.action(sql)
#     print t

# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,1):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                     select * from qn_guanning.guanninggame where ds<='2018-05-29'
#
#                   '''
#     result = hive_client.query(sql)
#     print t
#     f=open('guanninggame.txt','a+')
#     f.write('\n'.join(['\t'.join([str(y) for y in x]) for x in result]))
#     f.write('\n')
#     f.close()

    # d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
    # for t in range(0,60):
    #     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
    #     sql = '''
    #                 Insert overwrite table qn_guanning.guanninggamewithfeature
    #                 partition (ds='%s')
    #
    #                 select min(time),server,iid
    #                 ,concat_ws(';',collect_set(if(iswin>0,features,NULL))) as win_features
    #                 ,concat_ws(';',collect_set(if(iswin<0,features,NULL))) as lose_features
    #                 from (
    #                 select a.time,a.server,a.iid,a.id,if(b.features is null,'0,0,0,0,0,0,0,0,0,0,0,0,0,0',b.features) as features,iswin
    #                 from
    #                 (
    #                 SELECT time,server,iid,id,iswin
    #                 from qndb.h_guanning_result
    #                 where ds='%s'
    #                 )a
    #
    #                 left outer join
    #                 (select role_id,features from qn_guanning.guanningpersonal where ds='%s')b
    #                 on a.id=b.role_id
    #                 )c
    #                 group by server,iid
    #               '''%(date,date,date)

# d = datetime.datetime.strptime('2018-04-01', '%Y-%m-%d')
# for t in range(0,61):
#     date = (d+datetime.timedelta(t)).strftime('%Y-%m-%d')
#     sql = '''
#                       Insert overwrite table qn_guanning.guanningpersonal_one partition (ds='%s')
# select a.server,a.id,a.iid,concat_ws(',',a.seq,if(b.role_id is null,concat(repeat('0,',11),'0'),b.seq)
# ,if(c.role_id is null,concat(repeat('0,',12),'0'),c.seq))
# from  (select min(server) as server,id,iid,
#                              concat_ws(',',cast(round(avg(xiulian),2) as string)
# ,cast(round(avg(total_score),2) as string),cast(round(avg(help_num),2) as string)
# ,cast(round(avg(kill_score),2) as string),cast(round(avg(flag_score),2) as string)
# ,cast(round(avg(xiuwei),2) as string),cast(round(avg(equip_score),2) as string)
# ,cast(round(avg(team_score),2) as string),cast(round(avg(killed_score),2) as string)
# ,cast(round(avg(score_count),2) as string),cast(round(avg(grade),2) as string)
# ,cast(round(min(class),2) as string),cast(round(count(*),2) as string)) as seq
# from qndb.h_guanning_result where  ds='%s' group by id,iid)a
# left outer join
# (select
# role_id,scene_id,
# concat_ws(',',cast(round(max(maxhp),2) as string),cast(round(max(patt),2) as string)
# ,cast(round(max(matt),2) as string),cast(round(max(pdef),2) as string)
# ,cast(round(max(mdef),2) as string),cast(round(max(pmiss),2) as string)
# ,cast(round(max(mmiss),2) as string),cast(round(max(phit),2) as string)
# ,cast(round(max(mhit),2) as string),cast(round(max(pfatal),2) as string)
# ,cast(round(max(mfatal),2) as string),cast(round(max(pdef),2) as string)) as seq
# from qndb.h_guanning_roleinfo1 where ds='%s' group by role_id,scene_id)b
# on a.id=b.role_id and a.iid=b.scene_id
# left outer join
# (select
# role_id,scene_id,
# concat_ws(',',cast(round(max(block),2) as string),cast(round(max(ignoreblock),2) as string)
# ,cast(round(max(enhancedizzy),2) as string),cast(round(max(enhancemass),2) as string)
# ,cast(round(max(enhancesilence),2) as string),cast(round(max(antidizzy),2) as string)
# ,cast(round(max(antimass),2) as string),cast(round(max(antisilence),2) as string)
# ,cast(round(max(antiingorewater),2) as string),cast(round(max(antiingoreice),2) as string)
# ,cast(round(max(antiingorefire),2) as string),cast(round(max(antiingorethunder),2) as string)
# ,cast(round(max(xiuwei),2) as string)) as seq
# from qndb.h_guanning_roleinfo2 where ds='%s' group by role_id,scene_id)c
# on a.id=c.role_id and a.iid=c.scene_id
#
#                       '''%(date,date,date,date)
#     result = hive_client.action(sql)
#     print t
