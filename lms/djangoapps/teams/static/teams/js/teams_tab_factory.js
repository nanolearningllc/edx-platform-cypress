;(function (define) {
    'use strict';
    define([
        'jquery',
        'underscore',
        'backbone',
        'gettext',
        'teams/js/views/teams_tab',
        'teams/js/views/team_utils'
    ], function ($, _, Backbone, gettext, TeamsTabView, TeamUtils) {
            return function (options) {
                var teamsTab = new TeamsTabView({
                    el: $('.teams-content'),
                    context: options
                });
                $(document).ajaxError(function (event, xhr) {
                    var message;
                    if (xhr.status === 401) {
                        message = gettext("We couldn't complete your request. Please reload the page and try again.");
                    }
                    else if (xhr.status === 500) {
                        message = gettext("We had some trouble processing your request. Please try again.");
                    }
                    else {
                        return;
                    }
                    TeamUtils.showMessage(message);
                });
                teamsTab.start();
            };
        });
}).call(this, define || RequireJS.define);
