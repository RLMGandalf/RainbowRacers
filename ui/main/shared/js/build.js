
function BuildHotkeyModel() {
    var self = this;

    self.SpecIdToGridMap = ko.observable(
        {
			"/pa/units/land/laser_defense_single/laser_defense_single.json": ["factory", 11],
			"/pa/units/land/land_scout/land/scout.json": ["factory", 12]
        }
    );
};
