import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { NotebookCell, CommonDashboardState } from '../types';

export const initialCommonDashboardState: CommonDashboardState = {
  notebookCells: null,
  timeWindow: 'null',
  refreshBoolean: false,
  displayRealTime: true
};

export const commonDashboardSlice = createSlice({
  name: 'commondashboard',
  initialState: initialCommonDashboardState,
  reducers: {
    setTimeWindow: (state, action: PayloadAction<string>) => {
      state.timeWindow = action.payload;
    },
    setNotebookCells: (state, action: PayloadAction<NotebookCell[] | null>) => {
      state.notebookCells = action.payload;
    },
    refreshDashboards: state => {
      state.refreshBoolean = !state.refreshBoolean;
    },
    displayRealTime: (state, action: PayloadAction<boolean>) => {
      state.displayRealTime = action.payload;
    }
  }
});

export const {
  setTimeWindow,
  setNotebookCells,
  refreshDashboards,
  displayRealTime
} = commonDashboardSlice.actions;

export default commonDashboardSlice.reducer;
