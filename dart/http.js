import 'package:http/http.dart' as http;

main() async {
	var url = 'http://example.com/whasit/create';
	var response = await http.post(url, body: {'name': 'doodle', 'color': 'blue'});
	print(response.body);
}
