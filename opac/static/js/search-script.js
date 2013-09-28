(function($) {
	$('input#q').focus();
	var $themeCSS = $('link#theme-css');

	$('#theme-button').on('click', function () {
		if ( $(this).children('i').hasClass('icon-moon') ) {
			$(this).children('i').removeClass('icon-moon').addClass('icon-sun');
			// $themeCSS.attr('href','../static/css/search-night.css'); // not for localhost
			$themeCSS.attr('href','/static/css/search-night.css');
		} else {
			$(this).children('i').removeClass('icon-sun').addClass('icon-moon');
			// $themeCSS.attr('href','../static/css/search-day.css'); // not for localhost
			$themeCSS.attr('href','/static/css/search-day.css');
		}
	});
})(jQuery);

