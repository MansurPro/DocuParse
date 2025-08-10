#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to handle cleanup on script exit
cleanup() {
    echo -e "\n${YELLOW}Shutting down applications...${NC}"
    # Kill all background jobs started by this script
    jobs -p | xargs -r kill
    exit 0
}

# Set up trap to handle Ctrl+C
trap cleanup SIGINT SIGTERM

echo -e "${GREEN}Starting DocuParse Applications...${NC}"
echo -e "${BLUE}================================================${NC}"

# Start backend (FastAPI with uvicorn)
echo -e "${GREEN}Starting Backend (FastAPI)...${NC}"
uvicorn docuparse.fastapi_app:app --reload &
BACKEND_PID=$!

# Give backend a moment to start
sleep 2

# Start frontend (Gradio)
echo -e "${GREEN}Starting Frontend (Gradio)...${NC}"
python3 docuparse/gradio_app.py &
FRONTEND_PID=$!

echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}Both applications are starting up...${NC}"
echo -e "${YELLOW}Backend PID: $BACKEND_PID${NC}"
echo -e "${YELLOW}Frontend PID: $FRONTEND_PID${NC}"
echo -e "${BLUE}================================================${NC}"
echo -e "${RED}Press Ctrl+C to stop both applications${NC}"

# Wait for both processes
wait
