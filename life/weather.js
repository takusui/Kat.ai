// This script uses phantomjs to grab weather data from accuweather. 

var page = require('webpage').create();
page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36';

// Open the webpage.

page.open('https://www.accuweather.com/', function(status) {
    if (status != 'success') {
        console.log('No internet access.');
    } else {
        // Grab the weather of the current location (first element).

        var weather = page.evaluate(function() {
            var mainwthr = document.getElementsByClassName('day bg-su cl hv')[0]
                                   .getElementsByClassName('temp-set')[0];
            var loc = mainwthr.getElementsByClassName('loc')[0]
                               .getElementsByTagName('a')[0].textContent;
            var temp = mainwthr.getElementsByClassName('temp')[0]
                               .getElementsByClassName('large-temp')[0].textContent;
            var wthr = mainwthr.getElementsByClassName('cond')[0].textContent;

            temp = parseInt((parseInt(temp.substring(0,2)) - 32) * 5/9);

            return "The weather in " + loc + " is " + wthr + ", with a temperature of " + temp + " degrees celsius.";
        }); 
            console.log(weather); 
            // Find a way to return all 3 variables to modify them in python better. 
    }

    phantom.exit();

});