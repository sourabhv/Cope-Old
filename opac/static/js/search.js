(function ($) {

	var $logo = $('#logo');
	var $q = $('#q');
	var $view_buttons = $('#view-buttons').children('div');
	var $book_container = $('#book-container');
	var queryStringPrev = '';

	var min_height = $(window).innerHeight() - 70 - $('#container').children('header').outerHeight(true);
	$book_container.css({'min-height': min_height + 'px'});

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

	$('#search-button').on('click', function () {
		queryStringPrev = books_ajax_request(document.getElementById('q').value, queryStringPrev);
	});

	$q.on('keydown', function (e) {
		if (e.which == 13) {
			queryStringPrev = books_ajax_request(this.value, queryStringPrev);
			this.select();
		}
	})
}) (jQuery);

function books_ajax_request (queryString, queryStringPrev) {
	var $ = jQuery;
	var $title = $('title');

	queryString = $.trim(queryString)
	if (queryString.length == 0) {
		$('#book-container').empty();
	} else if (queryString != queryStringPrev) {
		$.ajax({
			type: 'GET',
			url: '/search/',
			data: {'q': queryString},
			content_type: 'application/json',
			dataType: 'json',
			success: function (data, statusText, jqXHR) {
				make_book_container(data);
				// history.pushState(null, queryString + ' | Cope', '?q='+queryString);
				document.title = queryString + ' | Cope | Library Search';
			},
			error: function (jqXHR, statusText, errorThrown) {
				// code
			}
		})
	}

	return queryString;
}

function make_book_container (BooksJSON) {
	var $ = jQuery;
	var $book_container = $('#book-container')

	var book_frame_tile_template = '\
<div class="book-frame" data-id="{{ pk }}">\
	<div class="book-inner-frame">\
		<img src="/static/images/{{ fields.imageurl}}" onError="this.onerror=null;this.src=\'/static/images/fallback_image.png\'">\
		<div class="book-details">\
			<div><div><i class="icon-user"></i></div>{{ fields.authors }}</div>\
			<div><div><i class="icon-file-text"></i></div>Edition: {{ fields.edition }}</div>\
			<div><div><i class="icon-truck"></i></div>{{ fields.publisher }}</div>\
			<div><div><i class="icon-book"></i></div>{{ fields.isbn }}</div>\
			<div><div><i class="icon-copy"></i></div>Copies left: {{ fields.copies_available }}</div>\
		</div>\
	</div>\
	<div class="book-name">{{ fields.title }}</div>\
</div>';

	var book_frame_list_template = '\
<div class="book-frame" data-id={{ pk }}>\
	<div class="book-inner-frame">\
		<img src="/static/images/djangoajax.png" onError="this.onerror=null;this.src=\'/static/images/fallback_image.png\'">\
		<div class="book-details">\
			<div class="book-name">{{ fields.title }}</div>\
			<div><div><i class="icon-user"></i></div>{{ fields.authors }}</div>\
			<div><div><i class="icon-file-text"></i></div>Edition: {{fields.edition}}</div>\
			<div><div><i class="icon-truck"></i></div>{{ fields.publisher }}</div>\
			<div><div><i class="icon-book"></i></div>{{ fields.isbn }}</div>\
			<div><div><i class="icon-copy"></i></div>Copies left: {{ fields.copies_available }}</div>\
		</div>\
	</div>\
</div>';

	$book_container.empty();
	$.each(BooksJSON, function () {
		if ($book_container.hasClass('list'))
			var book_frame_html = Mustache.to_html(book_frame_list_template, this);
		else
			var book_frame_html = Mustache.to_html(book_frame_tile_template, this);
		$book_container.append(book_frame_html);
	})

	// $book_container.html(JSON.stringify(BooksJSON, '', 4));
}
