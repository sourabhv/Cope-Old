(function($) {
	$('input#q').focus();
	var $themeCSS = $('link#theme-css');

	$('#theme-button').on('click', function () {
		if ( $(this).hasClass('icon-moon') ) {
			$(this).removeClass('icon-moon').addClass('icon-sun');
			// $themeCSS.attr('href','../static/css/search-night.css'); // not for localhost
			$themeCSS.attr('href','/static/css/search-results-night.css');
		} else {
			$(this).removeClass('icon-sun').addClass('icon-moon');
			// $themeCSS.attr('href','../static/css/search-day.css'); // not for localhost
			$themeCSS.attr('href','/static/css/search-results-day.css');
		}
	});
})(jQuery);
