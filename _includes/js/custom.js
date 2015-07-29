jQuery(document).ready(function() {
	$('#gf').text('GitHub Followers');
    $('#gfr').text('GitHub Repos');		
	
	JSONP( 'https://api.github.com/users/gkwelding?callback=?', function( response ) {
		var data = response.data;
		$('#gf').text(data.followers + ' GitHub Followers');
        $('#gfr').text(data.public_repos + ' GitHub Repos');
	});
	
	function JSONP( url, callback ) {
		var id = ( 'jsonp' + Math.random() * new Date() ).replace('.', '');
		var script = document.createElement('script');
		script.src = url.replace( 'callback=?', 'callback=' + id );
		document.body.appendChild( script );
		window[ id ] = function( data ) {
			if (callback) {
				callback( data );
			}
		};
	}	
	
	$('#ghw').githubWidget({
			'username': 'gkwelding',
			'displayActions': false,
			'firstCount': 10,
			'displayHeader': false,
			'displayLastCommit': false,
			'displayAccountInformations': false,
			'displayLanguage': false
    });
    
    function search() {
        $('#close', search).hide();
        var data = false;
        var matches = false;
        var search = $('#search');
        var find = function(phrase) {
            if(!data) {
                return $.ajax({
                    url: '/search.json',
                    dataType: 'json',
                    success: function(resp) {
                        data = _(resp).chain()
                            .compact()
                            .map(function(p) {
                                p.words = (p.title.toLowerCase() +' '+ p.summary.toLowerCase()).match(/(\w+)/g);
                                return p;
                            })
                            .value();
                        find(phrase);
                    }
                });
            }
            
            matches = _(data).filter(function(p) {
                return _(phrase).filter(function(a) {
                    return _(p.words).any(function(b) {
                        return a === b || b.indexOf(a) === 0;
                    });
                }).length === phrase.length;
            });
            
            $(matches).each(function(){
                $('#search-results', search).append('<li><h6>'+this.title+'</h6><p>'+this.title+'... <small><a href="'+this.url+'">Read more</a></small></p><hr></li>');
            });
            
            $('#search-results', search).show();
            $('#close', search).show();
        };
        $('input', search).bind("focus",_(function() {
            $('#search-results', search).empty();
            $('#search-results', search).hide();
            $('#close', search).hide();
            
            var phrase = $('input', search).val();
            if (phrase.length >= 4) {
                find(phrase.toLowerCase().match(/(\w+)/g));
            }
            return false;
        }).debounce(100));
        
        $('#close', search).bind("click", function() {
            $('#search-results', search).hide();
            $('#close', search).hide();
            return false;
        });
        
        $('input', search).keyup(_(function() {
            $('#search-results', search).empty();
            $('#search-results', search).hide();
            $('#close', search).hide();
            
            var phrase = $('input', search).val();
            if (phrase.length >= 4) {
                find(phrase.toLowerCase().match(/(\w+)/g));
            }
            return false;
        }).debounce(100));
    };
    search();
});