<h1> Работа с графом на JavaScript </h1>
<h3> Константы для работы функциями: </h3>

```
var graph = [ 1 , ... ]
var n = 64;
var WALL = 12;
var answ = new Array();
var used = new Array(n);

for(var i=0; i<n; i++)
{
	used[i] = 0;
}
  
```
<h3> Функции: </h3>

```
var HowVertex = function(used) // искомое кол-во недоступных вершин
{
    var answer=0;
    for(var i=0; i<25; i++)
    {
        if(used[i]===0)
        {
            answer++;
        }
    }

    return answer-WALL;
}

var CutAnsw = function(answ) // корректировка пути
{
    var a1 = [];
    var i = answ.lenght - 1;
    while(answ[i]<answ[i-1])
    {
        i--;
    }

    for(var j=i; j>=0; j--)
    {
        a1.push_back(answ[j]);
    }

    a1.reverse();
    return a1;
}

var IsEmpty = function() // необходимо сделать
{
    return true;
}

var EraseVertex = function(s) // удаление вершины (завал)
{
    for(var i=0; i<n; i++)
    {
        graph[s][i] = 0;
        graph[i][s] = 0;

    }
}

var dfs = function(x) // обход в глубину
{
    answ.push(x);
	print(x);
    used[x]=1;
    for (var i=0; i<64; i ++)
    {
        if (graph[x][i] === 1)
        {
	    if(used[i] === 0)
	    {
		if(IsEmpty())
		{
			dfs(i);
			answ.push(x);
			print(x);
		}
		else
		{
			EraseVertex(i);
			break;
		}
            }
	}
    }

    used[x] = 2;
}

var FindWay = function(s) // нахождение пути для трика
{
// s - начальная вершина
	
    dfs(s);
    answ = CutAnsw(answ);
	
    return answ;
}

var main = function()
{
	__interpretation_started_timestamp__ = Date.now();
	FindWay(0);
	return;
}
```
