
function BuildHotkeyModel() {
    var self = this;

    self.SpecIdToGridMap = ko.observable(
        {
			"/pa/units/land/laser_defense_single/laser_defense_single.json": ["factory", 11],
			"/pa/units/land/land_barrier/land_barrier.json": ["factory", 12],
			"/pa/units/land/land_scout/land_scout.json": ["factory", 13]
        }
    );
};
