// Copyright 2020-2023 The MathWorks, Inc.

import { fireEvent, render } from "../../test/utils/react-test";
import React from "react";
import OverlayTrigger from "./index";
import configureMockStore from "redux-mock-store";

import * as actions from "../../actions";
import * as actionCreators from "../../actionCreators";
import state from '../../test/utils/state' 

describe("OverlayTrigger Component", () => {
  let  mockStore;
  beforeEach(() => {

    mockStore = configureMockStore();

    const mockIntersectionObserver = jest.fn();
    mockIntersectionObserver.mockReturnValue({
      observe: () => null,
      unobserve: () => null,
      disconnect: () => null,
    });
    window.IntersectionObserver = mockIntersectionObserver;
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should render without crashing", () => {
    const { getByTitle } = render(<OverlayTrigger />);

    expect(getByTitle("tools icon")).toBeInTheDocument();
  });

  it("should close tutorial on click", () => {
    const { getByTestId, container } = render(<OverlayTrigger />);

    // grab the tutorial close button and click on it.
    const tutorialCloseBtn = getByTestId("tutorialCloseBtn");
    fireEvent.click(tutorialCloseBtn);

    // Check if the tutorial is not rendered as it was closed.
    const tutorial = container.querySelector("#trigger-tutorial");
    expect(tutorial).not.toBeInTheDocument();
  });

  it("should dispatch SET_TRIGGER_POSITION when overlay trigger is moved", async () => {
    const store = mockStore(state);
    // dispatching an action to setTriggerPosition to (22, 22) in the mockstore
    store.dispatch(actionCreators.setTriggerPosition(22, 22));

    const actionsFromStore = store.getActions();
    const expectedPayload = {
      type: actions.SET_TRIGGER_POSITION,
      x: 22,
      y: 22,
    };

    // Check if the action dispatched from mockstore is same as expected action
    expect(actionsFromStore).toEqual([expectedPayload]);
  });
});
