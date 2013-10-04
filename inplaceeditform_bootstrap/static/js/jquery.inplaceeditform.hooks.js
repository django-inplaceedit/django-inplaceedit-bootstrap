(function ($) {
    "use strict";
    var enableActionInplaceEditOriginal = $.inplaceeditform.methods.enableInplaceEditAction;
    var disableActionInplaceEditOriginal = $.inplaceeditform.methods.disableInplaceEditAction;
    $.inplaceeditform.extend({
        enableInplaceEditAction: function(inplace_span) {
            var self = $.inplaceeditform;
            enableActionInplaceEditOriginal();
            self.inplaceeditfields.attr("data-toggle", "tooltip");
            self.inplaceeditfields.attr("title","Double Click to Edit");
        },
        disableInplaceEditAction: function(inplace_span) {
            var self = $.inplaceeditform;
            disableActionInplaceEditOriginal();
            self.inplaceeditfields.removeAttr("data-toggle");
            self.inplaceeditfields.removeAttr("title");
        },
    });
})(jQuery);