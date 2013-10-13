(function ($) {

	var $logo = $('#logo');
	var $q = $('#q');
	var $search_button = $('#search-button')
	var $view_buttons = $('#view-buttons').children('div');
	var $book_container = $('#book-container');
	var queryStringPrev = '';

	$book_container.css({'min-height': $(window).innerHeight() + 'px'});

	$q.on('input', function (e) {
		$('#container').animate({scrollTop: $logo.outerHeight()}, 500);
		$(this).off('input');
	}).focus();

	$view_buttons.on('click', function (e) {
		if (!($(this).hasClass('active'))) {
			var oldSizeClass = $view_buttons.filter('.active').attr('data-sizeClass');
			var newSizeClass = $(this).attr('data-sizeClass');
			$(this).addClass('active').siblings('div').removeClass('active');
			$book_container.removeClass().addClass(newSizeClass);

			// prepend .book-name to .book-details for list view and
			// append back to .book-frame when switching from list to other views
			if ($(this).attr('data-sizeClass') == 'list') {
				$book_container.children('.book-frame').each(function (e) {
					$(this).children('.book-name').prependTo($(this).find('.book-details'));
				});
			} else if (oldSizeClass == 'list') {
				$book_container.children('.book-frame').each(function (e) {
					$(this).find('.book-name').appendTo(this);
				});
			}
		}
	});

	$search_button.on('click', function (e) {
		queryStringPrev = books_ajax_request($q.value, queryStringPrev);
	});

	$q.on('keydown', function (e) {
		if (e.which == 13) {
			queryStringPrev = books_ajax_request(this.value, queryStringPrev);
		}
	})
}) (jQuery);

function books_ajax_request (queryString, queryStringPrev) {
	var $ = jQuery;
	queryString = $.trim(queryString)
	if (queryString.length > 0 && queryString != queryStringPrev) {
		$.ajax({
			type: 'GET',
			url: '/search/',
			data: {'q': queryString},
			content_type: 'application/json',
			dataType: 'json',
			success: function (data, statusText, jqXHR) {
				// console.log('success::statusText: ' + statusText);
				make_book_container(data);
			},
			error: function (jqXHR, statusText, errorThrown) {
				console.log('error::statusText: ' + statusText);
				console.log('error::errorThrown: ' + errorThrown);
			}
		})
	}

	return queryString;
}

function make_book_container (BooksJSON) {
	var $ = jQuery;
	var book_frame_tile_template = '<div class=\"book-frame\"> <div class=\"book-inner-frame\"> <img src=\"/static/images/{{ imageurl}}\"> <div class=\"book-details\"> <div><div><i class=\"icon-book\"></i></div>{{ isbn }}</div> <div><div><i class=\"icon-user\"></i></div>{{ authors }}</div> <div><div><i class=\"icon-file-text\"></i></div>Edition: {{ edition }}</div> <div><div><i class=\"icon-truck\"></i></div>{{ publisher }}</div> <div><div><i class=\"icon-copy\"></i></div>{{ pages }}</div> </div> </div> <div class=\"book-name\">{{ title }}</div> </div>';
	var book_frame_list_template = '<div class=\"book-frame\"> <div class=\"book-inner-frame\"> <img src=\"/static/images/djangoajax.png\"> <div class=\"book-details\"> <div class=\"book-name\">{{ title }}</div> <div><div><i class=\"icon-book\"></i></div>{{ isbn }}</div> <div><div><i class=\"icon-user\"></i></div>{{ authors }}</div> <div><div><i class=\"icon-file-text\"></i></div>Edition: {{edition}}</div> <div><div><i class=\"icon-truck\"></i></div>{{ publisher }}</div> <div><div><i class=\"icon-copy\"></i></div>{{ pages }}</div> </div> </div> </div>';
	$book_container = $('#book-container')
	$book_container.empty();
	// $book_container.html(JSON.stringify(BooksJSON, '', 4))
	$.each(BooksJSON, function () {
		if ($book_container.hasClass('list'))
			var book_frame_html = Mustache.to_html(book_frame_list_template, this.fields);
		else
			var book_frame_html = Mustache.to_html(book_frame_tile_template, this.fields);
		$book_container.append(book_frame_html);
	})
}
