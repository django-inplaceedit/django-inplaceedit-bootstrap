(function ($) {
    "use strict";
    var enableActionInplaceEditOriginal = $.inplaceeditform.methods.enableInplaceEditAction;
    var disableActionInplaceEditOriginal = $.inplaceeditform.methods.disableInplaceEditAction;
    $.inplaceeditform.extend({
        enableInplaceEditAction: function(inplace_span) {
            var self = $.inplaceeditform;
            enableActionInplaceEditOriginal();
            self.inplaceeditfields.attr("data-toggle", "tooltip");
            self.inplaceeditfields.attr("title", self.opts.tooltipText);
        },
        disableInplaceEditAction: function(inplace_span) {
            var self = $.inplaceeditform;
            disableActionInplaceEditOriginal();
            self.inplaceeditfields.removeAttr("data-toggle");
            self.inplaceeditfields.removeAttr("title");
        },
        transformField: function (tags) {
            var self = $.inplaceeditform;
            var field = $(tags).find(self.opts.fieldTypes);
            field.addClass("form-control");
            field.css("padding-bottom", "0px");
            field.css("padding-top", "0px");
        }
    });
})(jQuery);