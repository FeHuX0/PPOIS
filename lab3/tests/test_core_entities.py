
from datetime import datetime
import pytest

from ecology.core.Biome import Biome
from ecology.core.Habitat import Habitat
from ecology.core.Region import Region
from ecology.core.MonitoringStation import MonitoringStation
from ecology.community.CitizenScientist import CitizenScientist
from ecology.community.ParkRanger import ParkRanger
from ecology.community.Researcher import Researcher
from ecology.monitoring.DataLogger import DataLogger
from ecology.monitoring.DataCollectionLog import DataCollectionLog
from ecology.monitoring.EnvironmentalSample import EnvironmentalSample
from ecology.monitoring.AlertNotification import AlertNotification
from ecology.monitoring.IncidentReport import IncidentReport
from ecology.species.EndangeredStatus import EndangeredStatus
from ecology.species.Species import Species
from ecology.exceptions.HabitatCapacityException import HabitatCapacityException
from ecology.exceptions.DataCollectionException import DataCollectionException
from ecology.exceptions.SampleContaminationException import SampleContaminationException
from ecology.exceptions.WeatherAlertException import WeatherAlertException
from ecology.exceptions.MonitoringStationOfflineException import MonitoringStationOfflineException

def mk_region():
    return Region(name="Testland", latitude=0.0, longitude=0.0)

def test_habitat_capacity_and_species_status_and_rename():
    biome = Biome(biome_type="Forest", climate="Temperate", average_rainfall_mm=1200.0)
    h = Habitat(code="H-1", area_hectares=10.0, biome=biome, capacity=1, resident_species=[])
    status = EndangeredStatus(status="least concern", legal_protection="None", population_threshold=0, review_date="2024-01-01")
    sp1 = Species(scientific_name="Sp1", common_name="One", trophic_level="Herbivore", conservation_status=status, typical_habitats=[])
    sp2 = Species(scientific_name="Sp2", common_name="Two", trophic_level="Carnivore", conservation_status=status, typical_habitats=[])
    h.register_species(sp1)
    assert h.available_capacity() == 0
    with pytest.raises(HabitatCapacityException):
        h.register_species(sp2)

    # Conservation status missing should raise
    s = Species(scientific_name="X", common_name="Y", trophic_level="Z", conservation_status=None, typical_habitats=[])
    with pytest.raises(Exception):
        s.ensure_status()
    s.rename_common("New")
    assert s.common_name == "New"

def test_monitoring_logger_sample_and_station_online_check():
    r = mk_region()
    st = MonitoringStation(station_id="ST-1", region=r, active=True)
    # DataLogger basic behavior
    logger = DataLogger(logger_id="DL-1", station=st)
    logger.record(1.0, "2025-01-01T00:00:00Z")
    logger.record(2.0, "2025-01-01T01:00:00Z")
    assert logger.data_points == [1.0, 2.0]

    # DataCollectionLog average and validation
    collector = CitizenScientist(member_id="C1", name="Casey")
    log = DataCollectionLog(log_id="LOG-1", collector=collector, station=st)
    log.record_value(3.0, "ok")
    log.record_value(5.0, "ok")
    assert 3.9 < log.average_value() < 4.1
    with pytest.raises(DataCollectionException):
        log.record_value(-1.0, "bad")

    # Station offline validation
    st.active = False
    with pytest.raises(MonitoringStationOfflineException):
        st.validate_online()

    # Sample validation
    researcher = Researcher(researcher_id="R1", name="Res", institution="Lab")
    sample = EnvironmentalSample(sample_id="S1", collected_by=researcher, station=st, sample_type="soil", integrity_score=0.5)
    with pytest.raises(SampleContaminationException):
        sample.validate(0.9)
    sample.adjust_integrity(0.95)
    sample.validate(0.9)

def test_alert_incident_ranger_workflow():
    r = mk_region()
    ranger = ParkRanger(ranger_id="PR1", name="Alex", assigned_region=r)
    alert = AlertNotification(alert_id="A1", title="Storm", severity="high", issued_for=r)
    alert.add_responder(ranger)
    assert ranger in alert.responders
    with pytest.raises(WeatherAlertException):
        AlertNotification(alert_id="A2", title="Weird", severity="weird", issued_for=r).ensure_severity()

    incident = IncidentReport(report_id="I1", description="Tree fallen", reported_by=ranger, occurred_at=datetime.utcnow(), severity="low")
    assert incident.short_summary().startswith("low:")
    incident.escalate("high")
    assert incident.severity == "high"
