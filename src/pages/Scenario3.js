import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function Scenario3() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>Subject: Concerns About Accuracy of Emotion AI for Mental Health Assessments</h1>
          <p className="text-muted">From: jc2563@companyC.com</p>
          <p className="text-muted">To: you@emoai.com</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Dear EmoAI Customer Support Team,
            <br />
            <br />
            I hope this email finds you well. My name is Josep Garcés, and I'm writing on behalf of Company C regarding some concerns raised about the Emotion AI software we use to assess mental health conditions.
            <br />
            <br />
            Recently, a user reported being flagged as “high risk” for anxiety, which caused them additional stress and feelings of stigma. We've since received similar feedback from other users, questioning both the accuracy and sensitivity of the assessments.
            <br />
            <br />
            Given our commitment to providing supportive and trustworthy mental health services, we need to address these issues urgently. We would appreciate your clarification regarding this matter, as it is critical to maintaining our users' confidence in our digital healthcare solutions. Please let us know your thoughts and next steps at your earliest convenience.
            <br />
            <br />
            Sincerely,
            <br />
            Josep Garcés
            <br />
            Chief Operating Officer
            <br />
            Company C
          </p>
        </Col>
      </Row>
      {/* Reply Section */}
      <Row className="mt-4">
        <Col>
          <Form>
            <Form.Group controlId="replyTextArea">
              <Form.Label>Reply:</Form.Label>
              <Form.Control as="textarea" rows={5} placeholder="Type your reply here..." />
            </Form.Group>
            <Button variant="primary" className="mt-3">Send</Button>
          </Form>
        </Col>
      </Row>
    </Container>
  );
}

export default Scenario3;