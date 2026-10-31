import math


def minimax_ab(curDepth, nodeIndex, maxTurn, scores, targetDepth, alpha, beta):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        max_eval = -math.inf
        eval_left = minimax_ab(curDepth + 1, nodeIndex * 2, False, scores, targetDepth, alpha, beta)
        max_eval = max(max_eval, eval_left)
        alpha = max(alpha, eval_left)
        if beta <= alpha:
            return max_eval


        eval_right = minimax_ab(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth, alpha, beta)
        max_eval = max(max_eval, eval_right)
        alpha = max(alpha, eval_right)
        return max_eval

    else:
        min_eval = math.inf

        eval_left = minimax_ab(curDepth + 1, nodeIndex * 2, True, scores, targetDepth, alpha, beta)
        min_eval = min(min_eval, eval_left)
        beta = min(beta, eval_left)
        if beta <= alpha:
            return min_eval


        eval_right = minimax_ab(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth, alpha, beta)
        min_eval = min(min_eval, eval_right)
        beta = min(beta, eval_right)
        return min_eval


scores = [3, 5, 17, 8, -2, 5, -1, 7]
treeDepth = int(math.log2(len(scores)))

optimal_value = minimax_ab(0, 0, True, scores, treeDepth, -math.inf, math.inf)
print(f"The optimal value with Alpha-Beta Pruning is: {optimal_value}")














