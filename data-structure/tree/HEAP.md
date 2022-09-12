# max heap

Heap 의 특성

- 부모는 2개의 자식만을 갖는다
- 부모는 자식보다 높은 값을 갖는다

**배열**을 이용해서 **tree / heap** 을 구현하는경우
모든 노드에 대한 검색은 **상수 시간 O(1)** 에 이루어 질수 있다.

how?
Array = [2,8,6,1,10,15,3,12,11] 의 경우,

1번의 자식을 구하려면
Array[3 * 2 + 1]을 하면 왼쪽 자식 노드
Array[3 * 2 + 2]를 하면 오른쪽 자식 노드가 참조가 된다.
즉, 한번에 특정 주소/메모리상 위치 를 가르키기 때문에 O(1) 이다.

Heap 의 가장 큰 연산은 **“Make Heap”** (heap 의 특성을 지키기 위해 필요한 연산) 이다.

make heap 연산에 핵심은, **heapify down**, 가장 낮은 leaf 부터 값을 채워나간다.

heapify down = O(logN) : O(h)

- while 문을 통해서 부모, 왼쪽 자식, 오른쪽 자식의 값을 비교해서 가장 큰 값과 부모의 자리를 바꾼다.
- while Array[parent] ≠ leafNode
- if max ≠ parent: Array[parent] = Array[max]
  parent = max

**make Heap = O(n) : O(nlogn)**

- for 문으로 for i in range(len(Array)-1, -1, -1): 리프노드부터 올라가면서 돌리고
- heapify_down(Array[i], len(Array)) 를 넘겨줘서 위에 로직을 돌린다.

**insert = O(logN)**

heapify up = O(logN)

heapify 를 하는경우, 부모랑 나만 비교를 하기 때문에 (다른 자식 노드랑은 비교를 하지 않아도 된다) logN 시간이 걸린다.

**find Max value O(1)**

- heap 의 성질을 봤을땐, max 값은 항상 root 노드의 값이기 때문에 O(1) 이 된다.

**delete Max O(logN)** : heapify down 연산의 속도

- leaf 노드에서 (마지막 인덱스) 를 root 로 갖고 오고 자식들과 비교하는 연산을 수행하며 자리를 다시 찾아 간다. (heapify down)

**To Summarize**

- why or when do we use Heap?
  - when we need to **find** the max value or a child of a certain node it can be done in O(1)
  - when we have a lot of **inserting**,
    as it can be done in O(logN) by using ‘heapify-up’
  - Also when we need to delete a certain node or value(max), deletion (find O(1)) can be done very quickly and all that’s left to do is ‘heapify-down’.
