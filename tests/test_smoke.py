from ai_quality_operations_copilot import classify_ticket


def test_high_risk_ticket_contract() -> None:
    result = classify_ticket("Customer reports an unauthorized refund request")
    assert result.classification == "high_risk_review"
    assert result.evidence_step == "SOP-04"
    assert result.reason


def test_access_ticket_contract() -> None:
    result = classify_ticket("Agent cannot login to the tool")
    assert result.classification == "access_issue"
    assert result.evidence_step == "SOP-02"


def test_standard_ticket_contract() -> None:
    result = classify_ticket("Customer asks for an order status update")
    assert result.classification == "standard_review"
    assert result.evidence_step == "SOP-01"


def test_empty_ticket_rejected():
    with pytest.raises(ValueError):
        classify_ticket("")

def test_empty_ticket_rejected():
    try:
        classify_ticket("")
    except ValueError:
        return
    raise AssertionError("Empty ticket should raise ValueError")