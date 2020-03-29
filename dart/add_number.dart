class spacecraft {
String name;
DateTime launchDate;

spacecraft(this.name, this.launchDate){

}

spacecraft.unlaunched(String name) : this(name, null);

int get launchYear =>
	launchDate?.year;

void describe() {
	print('spacecraft: $name');
	if (launchDate != null){
		int years =  DateTime.now().difference(launchDate).inDays ~/ 365;
	print(' Launched: $launchYear ($years years ago)');
	} else {
	print('Unlaunched');
	}
	
}
}
main(){
var voyager = spacecraft('voyager I', DateTime(1977, 9, 5));
voyager.describe();

var voyager3 = spacecraft('Voyager III',DateTime(2023,9,3));
voyager3.describe();
}
