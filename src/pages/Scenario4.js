import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function Scenario4() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>Subject: Ask for Suggestion for Applied Emotion AI in Our Real-Time Emotion Tracking</h1>
          <p className="text-muted">From: stacey@companyD.com</p>
          <p className="text-muted">To: you@emoai.com</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            To whom it may concern, 
            <br />
            <br />
            I hope this email finds you well. My name is Stacey Silver, and I represent Company D, an online meeting software company focused on empowering our users—many of whom are sales professionals—to achieve better performance in their presentations and consultations.
            <br />
            <br />
            We are currently exploring the integration of Emotion AI into our platform to provide our users with deeper insights into their audience's responses. Specifically, we aim to incorporate the following features:
            <ul>
              <li>Emotion Detection: Understand the audience's emotional reactions in real-time.</li>
              <li>Attention Measurement: Monitor participants' levels of attention during sessions.</li>
              <li>Engagement Assessment: Quantify how engaged the audience is throughout the meeting.</li>
              <li>Continuous Feature Development: Regularly evolving features to meet user needs.</li>
            </ul>
            To move forward, we are seeking technical consultation to help us refine our approach, address potential challenges, and ensure seamless integration of these capabilities into our platform.We would greatly appreciate an opportunity to discuss this further and learn from your expertise.
            <br />
            <br />
            Looking forward to your response.
            <br />
            <br />
            Best regards,
            <br />
            Stacey Silver
            <br />
            Product Manager
            <br />
            Company D [Video Company]
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

export default Scenario4;