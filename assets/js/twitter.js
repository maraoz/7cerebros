window.addEvent('domready', function () {
	var appendScript = function (src) {
		var attrs = {'type': 'text/javascript', 'src': src};
		var el = new Element('script', attrs);
		el.inject($(document.body));
	}
	if ($('twitter_div')) {
		appendScript('http://twitter.com/javascripts/blogger.js');
		appendScript('http://twitter.com/statuses/user_timeline/' +
			'7cerebros.json?callback=twitterCallback2&count=3');
	}
});
