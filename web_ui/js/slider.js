$( document ).ready(function() {
 
  function createHoverState (myobject){
    myobject.hover(function() {
      $(this).prev().toggleClass('hilite');
      var fre =((($(".ui-slider-range:first").css("width").split("px")[0])/248)*100).toFixed(0);
      var dc =((($(".ui-slider-range:last").css("width").split("px")[0])/248)*100).toFixed(0);
    
     $(".sliderfre > span:last").html(fre);
    $(".sliderdc > span:last").html(dc);
    });
    myobject.mousedown(function() {
      $(this).prev().addClass('dragging');
      $("*").mouseup(function() {
      var fre =((($(".ui-slider-range:first").css("width").split("px")[0])/248)*100).toFixed(0);
      var dc =((($(".ui-slider-range:last").css("width").split("px")[0])/248)*100).toFixed(0);
    
     $(".sliderfre > span:last").html(fre);
    $(".sliderdc > span:last").html(dc);
        $(myobject).prev().removeClass('dragging');
      });
    });
  }
  // 初始化
  $(".slider").slider({
    orientation: "horizontal",
    range: "min",
    max: 100,
    value: 0,
    animate: 1300
  });
 $(".red").slider( "value", 60);
  $(".blue").slider( "value", 100 );
  // $('.slider').each(function(index) {
  //   $(this).slider( "value", 75-index*(50/($('.slider').length-1)));
  // });
  
   createHoverState($(".slider span.ui-slider-handle"));

});
