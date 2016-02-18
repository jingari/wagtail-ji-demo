
	// init controller
	var controller = new ScrollMagic.Controller({globalSceneOptions: {triggerHook: "onLeave", duration: "600",logLevel: 3}});

	// build scenes

createScrollMagic();

function createScrollMagic() {
	// get all slides
		var slides = document.querySelectorAll("section.imgPanel");
		
		// create scene for every slide
		for (var i=0; i<slides.length; i++) {
			console.log("i ="+i);
			new ScrollMagic.Scene({
					triggerElement: slides[i]
				})
				.setPin(slides[i])
				.addIndicators() // add indicators (requires plugin)
				.addTo(controller);
		}
    /*jQuery('.imgPanel').each(function() {

 	var imagePanel = new ScrollMagic.Scene({triggerElement: '#'+jQuery(this).attr('id')})
					.setPin('#'+jQuery(this).attr('id'))
					.addIndicators()
					.addTo(controller);
					});
    */
}

