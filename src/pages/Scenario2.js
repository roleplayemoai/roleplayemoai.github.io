import React from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';

function Scenario2() {
  return (
    <Container className="p-4">
      {/* Email UI */}
      <Row className="border-bottom pb-3 mb-3">
        <Col>
          <h1>Subject: Proposal for Collaboration on Emotion AI for Internal Assessment</h1>
          <p className="text-muted">From: mgupta@companyB.com</p>
          <p className="text-muted">To: you@emoai.com</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Dear EmoAI Sale Representative,
            <br />
            <br />
            I'm Mahadi Gupta from Company B. We are exploring the use of your Emotion AI software to develop an internal tool for evaluating employee performance.
            <br />
            <br />
            We believe this collaboration presents a great opportunity to showcase your software's capabilities and position your company as a key partner for one of the largest global IT companies. If successful, we would be happy to feature your organization as a collaborator in our internal and external communications.
            <br />
            <br />
            We'd like to discuss this opportunity further, including how we can tailor your software to meet our specific needs. Please let me know a suitable time for a meeting to explore the next steps.
            <br />
            <br />
            Looking forward to your response.
            <br />
            <br />
            Best regards,
            <br />
            --
            <br />
            Mahadi Gupta
            <br />
            Senior Project Manager
            <br />
            Company B [Leading IT Company]
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

export default Scenario2;
