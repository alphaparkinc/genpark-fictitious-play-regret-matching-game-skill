"""MCP stdio server for Regret Matching Learner."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import RegretMatchingLearner

learner = RegretMatchingLearner(num_actions=3)

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "regret_step",
                        "description": "Update regret matching learner with action taken and counterfactual payoff vector",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "action_taken": {"type": "integer"},
                                "payoffs": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["action_taken", "payoffs"]
                        }
                    },
                    {
                        "name": "get_regret_strategy",
                        "description": "Get current instantaneous and historical average mixed strategies",
                        "inputSchema": {"type": "object"}
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "regret_step":
            act = int(args.get("action_taken", 0))
            payoffs = [float(p) for p in args.get("payoffs", [])]
            learner.update(act, payoffs)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"current_strategy": learner.get_strategy(), "average_strategy": learner.get_average_strategy()}}
        elif name == "get_regret_strategy":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"current_strategy": learner.get_strategy(), "average_strategy": learner.get_average_strategy()}}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
