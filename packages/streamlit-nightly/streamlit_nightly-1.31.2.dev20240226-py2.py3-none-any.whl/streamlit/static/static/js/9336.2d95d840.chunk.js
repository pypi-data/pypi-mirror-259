(self.webpackChunk_streamlit_app=self.webpackChunk_streamlit_app||[]).push([[9336],{99322:e=>{!function(t){if("undefined"!==typeof window){var n=!0,o=10,i="",r=0,a="",u=null,c="",s=!1,d={resize:1,click:1},l=128,f=!0,m=1,h="bodyOffset",g=h,p=!0,v="",y={},w=32,b=null,T=!1,E=!1,O="[iFrameSizer]",S=O.length,M="",I={max:1,min:1,bodyScroll:1,documentElementScroll:1},N="child",A=!0,k=window.parent,C="*",z=0,R=!1,x=null,L=16,F=1,P="scroll",D=P,j=window,q=function(){ee("onMessage function not defined")},H=function(){},W=function(){},B={height:function(){return ee("Custom height calculation function not defined"),document.documentElement.offsetHeight},width:function(){return ee("Custom width calculation function not defined"),document.body.scrollWidth}},J={},U=!1;try{var _=Object.create({},{passive:{get:function(){U=!0}}});window.addEventListener("test",K,_),window.removeEventListener("test",K,_)}catch(Oe){}var V={bodyOffset:function(){return document.body.offsetHeight+le("marginTop")+le("marginBottom")},offset:function(){return V.bodyOffset()},bodyScroll:function(){return document.body.scrollHeight},custom:function(){return B.height()},documentElementOffset:function(){return document.documentElement.offsetHeight},documentElementScroll:function(){return document.documentElement.scrollHeight},max:function(){return Math.max.apply(null,me(V))},min:function(){return Math.min.apply(null,me(V))},grow:function(){return V.max()},lowestElement:function(){return Math.max(V.bodyOffset()||V.documentElementOffset(),fe("bottom",ge()))},taggedElement:function(){return he("bottom","data-iframe-height")}},X={bodyScroll:function(){return document.body.scrollWidth},bodyOffset:function(){return document.body.offsetWidth},custom:function(){return B.width()},documentElementScroll:function(){return document.documentElement.scrollWidth},documentElementOffset:function(){return document.documentElement.offsetWidth},scroll:function(){return Math.max(X.bodyScroll(),X.documentElementScroll())},max:function(){return Math.max.apply(null,me(X))},min:function(){return Math.min.apply(null,me(X))},rightMostElement:function(){return fe("right",ge())},taggedElement:function(){return he("right","data-iframe-width")}},Y=function(e){var t,n,o,i=null,r=0,a=function(){r=Date.now(),i=null,o=e.apply(t,n),i||(t=n=null)};return function(){var u=Date.now();r||(r=u);var c=L-(u-r);return t=this,n=arguments,c<=0||c>L?(i&&(clearTimeout(i),i=null),r=u,o=e.apply(t,n),i||(t=n=null)):i||(i=setTimeout(a,c)),o}}(pe);Q(window,"message",(function(n){var o={init:function(){v=n.data,k=n.source,te(),f=!1,setTimeout((function(){p=!1}),l)},reset:function(){p?$("Page reset ignored by init"):($("Page size reset by host page"),we("resetPage"))},resize:function(){ve("resizeParent","Parent window requested size check")},moveToAnchor:function(){y.findTarget(r())},inPageLink:function(){this.moveToAnchor()},pageInfo:function(){var e=r();$("PageInfoFromParent called from parent: "+e),W(JSON.parse(e)),$(" --")},message:function(){var e=r();$("onMessage called from parent: "+e),q(JSON.parse(e)),$(" --")}};function i(){return n.data.split("]")[1].split(":")[0]}function r(){return n.data.slice(n.data.indexOf(":")+1)}function a(){return n.data.split(":")[2]in{true:1,false:1}}function u(){var r=i();r in o?o[r]():!e.exports&&"iFrameResize"in window||window.jQuery!==t&&"iFrameResize"in window.jQuery.prototype||a()||ee("Unexpected message ("+n.data+")")}O===(""+n.data).slice(0,S)&&(!1===f?u():a()?o.init():$('Ignored message of type "'+i()+'". Received before initialization.'))})),Q(window,"readystatechange",Ee),Ee()}function K(){}function Q(e,t,n,o){e.addEventListener(t,n,!!U&&(o||{}))}function G(e){return e.charAt(0).toUpperCase()+e.slice(1)}function Z(e){return O+"["+M+"] "+e}function $(e){T&&"object"===typeof window.console&&console.log(Z(e))}function ee(e){"object"===typeof window.console&&console.warn(Z(e))}function te(){!function(){function e(e){return"true"===e}var o=v.slice(S).split(":");M=o[0],r=t===o[1]?r:Number(o[1]),s=t===o[2]?s:e(o[2]),T=t===o[3]?T:e(o[3]),w=t===o[4]?w:Number(o[4]),n=t===o[6]?n:e(o[6]),a=o[7],g=t===o[8]?g:o[8],i=o[9],c=o[10],z=t===o[11]?z:Number(o[11]),y.enable=t!==o[12]&&e(o[12]),N=t===o[13]?N:o[13],D=t===o[14]?D:o[14],E=t===o[15]?E:Boolean(o[15])}(),$("Initialising iFrame ("+window.location.href+")"),function(){function e(){var e=window.iFrameResizer;$("Reading data from page: "+JSON.stringify(e)),Object.keys(e).forEach(ne,e),q="onMessage"in e?e.onMessage:q,H="onReady"in e?e.onReady:H,C="targetOrigin"in e?e.targetOrigin:C,g="heightCalculationMethod"in e?e.heightCalculationMethod:g,D="widthCalculationMethod"in e?e.widthCalculationMethod:D}function t(e,t){return"function"===typeof e&&($("Setup custom "+t+"CalcMethod"),B[t]=e,e="custom"),e}"iFrameResizer"in window&&Object===window.iFrameResizer.constructor&&(e(),g=t(g,"height"),D=t(D,"width"));$("TargetOrigin for parent set to: "+C)}(),function(){t===a&&(a=r+"px");oe("margin",function(e,t){-1!==t.indexOf("-")&&(ee("Negative CSS value ignored for "+e),t="");return t}("margin",a))}(),oe("background",i),oe("padding",c),function(){var e=document.createElement("div");e.style.clear="both",e.style.display="block",e.style.height="0",document.body.appendChild(e)}(),ue(),ce(),document.documentElement.style.height="",document.body.style.height="",$('HTML & body height set to "auto"'),$("Enable public methods"),j.parentIFrame={autoResize:function(e){return!0===e&&!1===n?(n=!0,se()):!1===e&&!0===n&&(n=!1,re("remove"),null!==u&&u.disconnect(),clearInterval(b)),Te(0,0,"autoResize",JSON.stringify(n)),n},close:function(){Te(0,0,"close")},getId:function(){return M},getPageInfo:function(e){"function"===typeof e?(W=e,Te(0,0,"pageInfo")):(W=function(){},Te(0,0,"pageInfoStop"))},moveToAnchor:function(e){y.findTarget(e)},reset:function(){be("parentIFrame.reset")},scrollTo:function(e,t){Te(t,e,"scrollTo")},scrollToOffset:function(e,t){Te(t,e,"scrollToOffset")},sendMessage:function(e,t){Te(0,0,"message",JSON.stringify(e),t)},setHeightCalculationMethod:function(e){g=e,ue()},setWidthCalculationMethod:function(e){D=e,ce()},setTargetOrigin:function(e){$("Set targetOrigin: "+e),C=e},size:function(e,t){ve("size","parentIFrame.size("+(e||"")+(t?","+t:"")+")",e,t)}},function(){if(!0!==E)return;function e(e){Te(0,0,e.type,e.screenY+":"+e.screenX)}function t(t,n){$("Add event listener: "+n),Q(window.document,t,e)}t("mouseenter","Mouse Enter"),t("mouseleave","Mouse Leave")}(),se(),y=function(){function e(){return{x:window.pageXOffset===t?document.documentElement.scrollLeft:window.pageXOffset,y:window.pageYOffset===t?document.documentElement.scrollTop:window.pageYOffset}}function n(t){var n=t.getBoundingClientRect(),o=e();return{x:parseInt(n.left,10)+parseInt(o.x,10),y:parseInt(n.top,10)+parseInt(o.y,10)}}function o(e){function o(e){var t=n(e);$("Moving to in page link (#"+i+") at x: "+t.x+" y: "+t.y),Te(t.y,t.x,"scrollToOffset")}var i=e.split("#")[1]||e,r=decodeURIComponent(i),a=document.getElementById(r)||document.getElementsByName(r)[0];t===a?($("In page link (#"+i+") not found in iFrame, so sending to parent"),Te(0,0,"inPageLink","#"+i)):o(a)}function i(){var e=window.location.hash,t=window.location.href;""!==e&&"#"!==e&&o(t)}function r(){function e(e){function t(e){e.preventDefault(),o(this.getAttribute("href"))}"#"!==e.getAttribute("href")&&Q(e,"click",t)}Array.prototype.forEach.call(document.querySelectorAll('a[href^="#"]'),e)}function a(){Q(window,"hashchange",i)}function u(){setTimeout(i,l)}function c(){Array.prototype.forEach&&document.querySelectorAll?($("Setting up location.hash handlers"),r(),a(),u()):ee("In page linking not fully supported in this browser! (See README.md for IE8 workaround)")}y.enable?c():$("In page linking not enabled");return{findTarget:o}}(),ve("init","Init message from host page"),H()}function ne(e){var t=e.split("Callback");if(2===t.length){var n="on"+t[0].charAt(0).toUpperCase()+t[0].slice(1);this[n]=this[e],delete this[e],ee("Deprecated: '"+e+"' has been renamed '"+n+"'. The old method will be removed in the next major version.")}}function oe(e,n){t!==n&&""!==n&&"null"!==n&&(document.body.style[e]=n,$("Body "+e+' set to "'+n+'"'))}function ie(e){var t={add:function(t){function n(){ve(e.eventName,e.eventType)}J[t]=n,Q(window,t,n,{passive:!0})},remove:function(e){var t,n,o,i=J[e];delete J[e],t=window,n=e,o=i,t.removeEventListener(n,o,!1)}};e.eventNames&&Array.prototype.map?(e.eventName=e.eventNames[0],e.eventNames.map(t[e.method])):t[e.method](e.eventName),$(G(e.method)+" event listener: "+e.eventType)}function re(e){ie({method:e,eventType:"Animation Start",eventNames:["animationstart","webkitAnimationStart"]}),ie({method:e,eventType:"Animation Iteration",eventNames:["animationiteration","webkitAnimationIteration"]}),ie({method:e,eventType:"Animation End",eventNames:["animationend","webkitAnimationEnd"]}),ie({method:e,eventType:"Input",eventName:"input"}),ie({method:e,eventType:"Mouse Up",eventName:"mouseup"}),ie({method:e,eventType:"Mouse Down",eventName:"mousedown"}),ie({method:e,eventType:"Orientation Change",eventName:"orientationchange"}),ie({method:e,eventType:"Print",eventNames:["afterprint","beforeprint"]}),ie({method:e,eventType:"Ready State Change",eventName:"readystatechange"}),ie({method:e,eventType:"Touch Start",eventName:"touchstart"}),ie({method:e,eventType:"Touch End",eventName:"touchend"}),ie({method:e,eventType:"Touch Cancel",eventName:"touchcancel"}),ie({method:e,eventType:"Transition Start",eventNames:["transitionstart","webkitTransitionStart","MSTransitionStart","oTransitionStart","otransitionstart"]}),ie({method:e,eventType:"Transition Iteration",eventNames:["transitioniteration","webkitTransitionIteration","MSTransitionIteration","oTransitionIteration","otransitioniteration"]}),ie({method:e,eventType:"Transition End",eventNames:["transitionend","webkitTransitionEnd","MSTransitionEnd","oTransitionEnd","otransitionend"]}),"child"===N&&ie({method:e,eventType:"IFrame Resized",eventName:"resize"})}function ae(e,t,n,o){return t!==e&&(e in n||(ee(e+" is not a valid option for "+o+"CalculationMethod."),e=t),$(o+' calculation method set to "'+e+'"')),e}function ue(){g=ae(g,h,V,"height")}function ce(){D=ae(D,P,X,"width")}function se(){!0===n?(re("add"),function(){var e=0>w;window.MutationObserver||window.WebKitMutationObserver?e?de():u=function(){function e(e){function t(e){!1===e.complete&&($("Attach listeners to "+e.src),e.addEventListener("load",i,!1),e.addEventListener("error",r,!1),c.push(e))}"attributes"===e.type&&"src"===e.attributeName?t(e.target):"childList"===e.type&&Array.prototype.forEach.call(e.target.querySelectorAll("img"),t)}function t(e){c.splice(c.indexOf(e),1)}function n(e){$("Remove listeners from "+e.src),e.removeEventListener("load",i,!1),e.removeEventListener("error",r,!1),t(e)}function o(e,t,o){n(e.target),ve(t,o+": "+e.target.src)}function i(e){o(e,"imageLoad","Image loaded")}function r(e){o(e,"imageLoadFailed","Image load failed")}function a(t){ve("mutationObserver","mutationObserver: "+t[0].target+" "+t[0].type),t.forEach(e)}function u(){var e=document.querySelector("body"),t={attributes:!0,attributeOldValue:!1,characterData:!0,characterDataOldValue:!1,childList:!0,subtree:!0};return d=new s(a),$("Create body MutationObserver"),d.observe(e,t),d}var c=[],s=window.MutationObserver||window.WebKitMutationObserver,d=u();return{disconnect:function(){"disconnect"in d&&($("Disconnect body MutationObserver"),d.disconnect(),c.forEach(n))}}}():($("MutationObserver not supported in this browser!"),de())}()):$("Auto Resize disabled")}function de(){0!==w&&($("setInterval: "+w+"ms"),b=setInterval((function(){ve("interval","setInterval: "+w)}),Math.abs(w)))}function le(e,t){var n=0;return t=t||document.body,n=null===(n=document.defaultView.getComputedStyle(t,null))?0:n[e],parseInt(n,o)}function fe(e,t){for(var n=t.length,o=0,i=0,r=G(e),a=Date.now(),u=0;u<n;u++)(o=t[u].getBoundingClientRect()[e]+le("margin"+r,t[u]))>i&&(i=o);return a=Date.now()-a,$("Parsed "+n+" HTML elements"),$("Element position calculated in "+a+"ms"),function(e){e>L/2&&$("Event throttle increased to "+(L=2*e)+"ms")}(a),i}function me(e){return[e.bodyOffset(),e.bodyScroll(),e.documentElementOffset(),e.documentElementScroll()]}function he(e,t){var n=document.querySelectorAll("["+t+"]");return 0===n.length&&(ee("No tagged elements ("+t+") found on page"),document.querySelectorAll("body *")),fe(e,n)}function ge(){return document.querySelectorAll("body *")}function pe(e,n,o,i){var r,a;!function(){function e(e,t){return!(Math.abs(e-t)<=z)}return r=t===o?V[g]():o,a=t===i?X[D]():i,e(m,r)||s&&e(F,a)}()&&"init"!==e?!(e in{init:1,interval:1,size:1})&&(g in I||s&&D in I)?be(n):e in{interval:1}||$("No change in size detected"):(ye(),Te(m=r,F=a,e))}function ve(e,t,n,o){R&&e in d?$("Trigger event cancelled: "+e):(e in{reset:1,resetPage:1,init:1}||$("Trigger event: "+t),"init"===e?pe(e,t,n,o):Y(e,t,n,o))}function ye(){R||(R=!0,$("Trigger event lock on")),clearTimeout(x),x=setTimeout((function(){R=!1,$("Trigger event lock off"),$("--")}),l)}function we(e){m=V[g](),F=X[D](),Te(m,F,e)}function be(e){var t=g;g=h,$("Reset trigger event: "+e),ye(),we("reset"),g=t}function Te(e,n,o,i,r){!0===A&&(t===r?r=C:$("Message targetOrigin: "+r),function(){var a=M+":"+e+":"+n+":"+o+(t===i?"":":"+i);$("Sending message to host page ("+a+")"),k.postMessage(O+a,r)}())}function Ee(){"loading"!==document.readyState&&window.parent.postMessage("[iFrameResizerChild]Ready","*")}}()}}]);