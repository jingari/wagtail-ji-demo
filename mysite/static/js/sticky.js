
// init controller
var controller = new ScrollMagic.Controller();

// create a scene
new ScrollMagic.Scene({
        //duration: 100,  // the scene should last for a scroll distance of 100px
        offset: 50      // start this scene after scrolling for 50px
    })
    .setPin(".sticky") // pins the element for the the scene's duration
    .addTo(controller); // assign the scene to the controller

/*
var slides = document.querySelectorAll("section.pull-quote-wrapper");
for (var i=0; i<slides.length; i++) {
			new ScrollMagic.Scene({
					triggerElement: slides[i]
				})
				.setPin(slides[i])
				//.addIndicators() // add indicators (requires plugin)
				.addTo(controller);
		}
*/
