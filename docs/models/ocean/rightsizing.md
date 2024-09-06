<h1 id="spotinst_sdk2.models.ocean.rightsizing">spotinst_sdk2.models.ocean.rightsizing</h1>


<h2 id="spotinst_sdk2.models.ocean.rightsizing.IntervalHours">IntervalHours</h2>

```python
IntervalHours(self,
              start_time: str = 'd3043820717d74d9a17694c176d39733',
              end_time: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __start_time__: str
- __end_time__: str

<h2 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays">IntervalDays</h2>

```python
IntervalDays(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Friday">Friday</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Monday">Monday</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Saturday">Saturday</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Sunday">Sunday</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Thursday">Thursday</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Tuesday">Tuesday</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.IntervalDays.Wednesday">Wednesday</h3>


<h2 id="spotinst_sdk2.models.ocean.rightsizing.WeeklyRepetitionBasis">WeeklyRepetitionBasis</h2>

```python
WeeklyRepetitionBasis(
  self,
  interval_days:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.IntervalDays] = 'd3043820717d74d9a17694c176d39733',
  interval_hours: IntervalHours = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __interval_days__: List[IntervalDays]
- __interval_hours__: IntervalHours

<h2 id="spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth">WeekOfTheMonth</h2>

```python
WeekOfTheMonth(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth.First">First</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth.Fourth">Fourth</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth.Last">Last</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth.Second">Second</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth.Third">Third</h3>


<h2 id="spotinst_sdk2.models.ocean.rightsizing.MonthlyRepetitionBasis">MonthlyRepetitionBasis</h2>

```python
MonthlyRepetitionBasis(
    self,
    interval_months: typing.List[int] = 'd3043820717d74d9a17694c176d39733',
    week_of_the_month:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.WeekOfTheMonth] = 'd3043820717d74d9a17694c176d39733',
    weekly_repetition_basis:
    WeeklyRepetitionBasis = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __interval_months__: List[int]
- __week_of_the_month__: List[WeekOfTheMonth]
- __weekly_repetition_basis__: WeeklyRepetitionBasis

<h2 id="spotinst_sdk2.models.ocean.rightsizing.RepetitionBasis">RepetitionBasis</h2>

```python
RepetitionBasis(cls,
                value,
                names=None,
                *,
                module,
                qualname,
                type,
                start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.rightsizing.RepetitionBasis.Monthly">Monthly</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.RepetitionBasis.Weekly">Weekly</h3>


<h2 id="spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationInterval">RecommendationApplicationInterval</h2>

```python
RecommendationApplicationInterval(
    self,
    repetition_basis: RepetitionBasis = 'd3043820717d74d9a17694c176d39733',
    monthly_repetition_basis:
    MonthlyRepetitionBasis = 'd3043820717d74d9a17694c176d39733',
    weekly_repetition_basis:
    WeeklyRepetitionBasis = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __repetition_basis__: RepetitionBasis
- __monthly_repetition_basis__: MonthlyRepetitionBasis
- __weekly_repetition_basis__: WeeklyRepetitionBasis

<h2 id="spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationMinThreshold">RecommendationApplicationMinThreshold</h2>

```python
RecommendationApplicationMinThreshold(
  self,
  cpu_percentage: float = 'd3043820717d74d9a17694c176d39733',
  memory_percentage: float = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_percentage__: float
- __memory_percentage__: float

<h2 id="spotinst_sdk2.models.ocean.rightsizing.CPU">CPU</h2>

```python
CPU(self,
    min: int = 'd3043820717d74d9a17694c176d39733',
    max: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __min__: int
- __max__: int

<h2 id="spotinst_sdk2.models.ocean.rightsizing.Memory">Memory</h2>

```python
Memory(self,
       min: int = 'd3043820717d74d9a17694c176d39733',
       max: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __min__: int
- __max__: int

<h2 id="spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationBoundaries">RecommendationApplicationBoundaries</h2>

```python
RecommendationApplicationBoundaries(
  self,
  cpu: CPU = 'd3043820717d74d9a17694c176d39733',
  memory: Memory = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu__: CPU
- __memory__: Memory

<h2 id="spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationOverheadValues">RecommendationApplicationOverheadValues</h2>

```python
RecommendationApplicationOverheadValues(
  self,
  cpu_percentage: float = 'd3043820717d74d9a17694c176d39733',
  memory_percentage: float = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_percentage__: float
- __memory_percentage__: float

<h2 id="spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationHPA">RecommendationApplicationHPA</h2>

```python
RecommendationApplicationHPA(
  self,
  allow_h_p_a_recommendations: bool = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __allow_h_p_a_recommendations__: bool

<h2 id="spotinst_sdk2.models.ocean.rightsizing.Label">Label</h2>

```python
Label(self,
      key: str = 'd3043820717d74d9a17694c176d39733',
      value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.rightsizing.Workload">Workload</h2>

```python
Workload(self,
         name: str = 'd3043820717d74d9a17694c176d39733',
         workload_type: str = 'd3043820717d74d9a17694c176d39733',
         regex_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __workload_type__: str
- __regex_name__: str

<h2 id="spotinst_sdk2.models.ocean.rightsizing.Namespace">Namespace</h2>

```python
Namespace(
    self,
    namespace_name: str = 'd3043820717d74d9a17694c176d39733',
    labels:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.Label] = 'd3043820717d74d9a17694c176d39733',
    workloads:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.Workload] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __namespace_name__: str
- __labels__: List[Label]
- __workloads__: List[Workload]

<h2 id="spotinst_sdk2.models.ocean.rightsizing.ClusterResources">ClusterResources</h2>

```python
ClusterResources(self, data: dict)
```

__Arguments__

- __data__: dict

<h2 id="spotinst_sdk2.models.ocean.rightsizing.ClusterLabels">ClusterLabels</h2>

```python
ClusterLabels(self, data: dict)
```

__Arguments__

- __data__: dict

<h2 id="spotinst_sdk2.models.ocean.rightsizing.RestartReplicas">RestartReplicas</h2>

```python
RestartReplicas(cls,
                value,
                names=None,
                *,
                module,
                qualname,
                type,
                start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.rightsizing.RestartReplicas.All_manifest">All_manifest</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.RestartReplicas.More_than_one_replica">More_than_one_replica</h3>


<h3 id="spotinst_sdk2.models.ocean.rightsizing.RestartReplicas.No_restart">No_restart</h3>


