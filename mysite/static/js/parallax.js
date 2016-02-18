
	// init controller
	var controller = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onEnter", duration: "200%"}});

	// build scenes
	//new ScrollMagic.Scene({triggerElement: "#parallax0"})
	/*new ScrollMagic.Scene({triggerElement: "#parallax2"})
					.setTween("#parallax2 > div", {y: "80%", ease: Linear.easeNone})
					.addIndicators()
					.addTo(controller);

	new ScrollMagic.Scene({triggerElement: "#parallax3"})
					.setTween("#parallax3 > div", {y: "80%", ease: Linear.easeNone})
					.addIndicators()
					.addTo(controller);

	new ScrollMagic.Scene({triggerElement: "#parallax4"})
					.setTween("#parallax4 > div", {y: "80%", ease: Linear.easeNone})
					.addIndicators()
					.addTo(controller);*/

createScrollMagic();

function createScrollMagic() {

    jQuery('.parallaxParent').each(function() {

    	var paraScene = new ScrollMagic.Scene({triggerElement: '#'+jQuery(this).attr('id')})
					.setTween('#'+jQuery(this).attr('id')+' > div', {y: "80%", ease: Linear.easeNone})
					.addIndicators()
					.addTo(controller);
					});
        /*var cardTween = TweenMax.fromTo('#'+$(this).attr('id')+' .wrap', 1,
            {
                scale: 0,
                // z: 1,
                y: 500,
                x: 800,
                skewX: '200deg',
                transformPerspective: 200,
                rotation: '10deg'
            },
            {
                scale: 1,
                // z: 1,
                y: 0,
                x: 0,
                skewX: 0,
                rotation: 0
            }
        );*/
/*
        var cardScene = new ScrollScene({
            triggerElement: '#'+$(this).attr('id'),
            duration: $(window).height() * 0.7,
            offset: -250
        })
        .addTo(scrollMagicController)
        .setTween(cardTween);
    */
}

/*


		// init
		var controller = new ScrollMagic.Controller({
			globalSceneOptions: {
				triggerHook: 'onLeave'
			}
		});

		// get all slides
		var slides = document.querySelectorAll("section.panel");

		// create scene for every slide
		for (var i=0; i<slides.length; i++) {
			new ScrollMagic.Scene({
					triggerElement: slides[i]
				})
				.setPin(slides[i])
				.addIndicators() // add indicators (requires plugin)
				.addTo(controller);
		}
*/