define(['jquery', 'backbone', 'models/search', 'views/search_result'], function ($, Backbone, SearchModel, SearchResultView) {
    return Backbone.Collection.extend({
        model: SearchModel,
        url: "/api/search/",
        viewCollection: [],
        sidePanel: null,
        searchValue: '',
        search: function (searchValue, sidePanel) {
            this.searchValue = searchValue;
            this.url = this.url + searchValue;
            this.sidePanel = sidePanel;
        },
        renderCollection: function () {
            var self = this;
            this.sidePanel.updateSidePanelTitle('Search results for ' + this.searchValue);
            $.each(this.viewCollection, function (index, view) {
                view.destroy();
            });
            this.viewCollection = [];
            $.each(this.models, function (index, model) {
                self.viewCollection.push(new SearchResultView({
                    model: model,
                    sidePanel: self.sidePanel
                }));
            });
        }
    })
});
