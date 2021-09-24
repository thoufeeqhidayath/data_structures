################dict union###############
p = {"hello":"S"}
n = {**p,"hello":"d"}
print(n)


#########dict sorting########################
from collections import defaultdict
from datetime import datetime

from bson import ObjectId

s = [{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b092'),
  'precedence_order': 1,
 },
{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b092'),
  'precedence_order': 1,
 },
{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b092'),
  'precedence_order': 5,
 },

{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b093'),
  'precedence_order': 1,
 },

{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b093'),
  'precedence_order': 2,
 },
{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b093'),
  'precedence_order': 3,
 },
{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',
  'persona_id': ObjectId('608fc96dd368664f2713b093'),
  'precedence_order': 4,
 },
{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97c',
  'persona_id': ObjectId('608fc96dd368664f2713b092'),
  'precedence_order': 0}  ,
{
  'activity_id': 'ecefc912485362c8fc3f8ec148c33f4c944529330479c8073987fde554eee97b',

  'persona_id': ObjectId('608fc96dd368664f2713b092'),
  'precedence_order': 2
 }


]

s.sort(key=lambda x: (x.get('persona_id'),x.get('activity_id',''), x.get('precedence_order',0)))
for item in s:
    print(item)
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(s)
sorted_df = unsorted_df.sort_values(by=['persona_id', 'activity_id',"precedence_order"])

print(sorted_df.to_dict())




######################
