Stream<int> timedCounter(Duration interval, [int maxc]) async* {
int i=0;
while (true) {
await Future.delayed(interval);
yield i++;
if(i==maxc) break;
}
}

main() async{
	await for (var val in timedCounter(Duration(seconds:2),2)){
print('new val is $val');
}

}
