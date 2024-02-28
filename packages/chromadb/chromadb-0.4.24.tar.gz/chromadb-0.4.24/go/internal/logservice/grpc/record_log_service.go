package grpc

import (
	"context"
	"github.com/chroma/chroma-coordinator/internal/grpcutils"
	"github.com/chroma/chroma-coordinator/internal/proto/coordinatorpb"
	"github.com/chroma/chroma-coordinator/internal/proto/logservicepb"
	"github.com/chroma/chroma-coordinator/internal/types"
	"github.com/pingcap/log"
	"go.uber.org/zap"
	"google.golang.org/protobuf/proto"
)

func (s *Server) PushLogs(ctx context.Context, req *logservicepb.PushLogsRequest) (*logservicepb.PushLogsResponse, error) {
	res := &logservicepb.PushLogsResponse{}
	collectionID, err := types.ToUniqueID(&req.CollectionId)
	err = grpcutils.BuildErrorForCollectionId(collectionID, err)
	if err != nil {
		return nil, err
	}
	var recordsContent [][]byte
	for _, record := range req.Records {
		record.CollectionId = ""
		data, err := proto.Marshal(record)
		if err != nil {
			log.Error("marshaling error", zap.Error(err))
			grpcError, err := grpcutils.BuildInvalidArgumentGrpcError("records", "marshaling error")
			if err != nil {
				return nil, err
			}
			return nil, grpcError
		}
		recordsContent = append(recordsContent, data)
	}
	recordCount, err := s.logService.PushLogs(ctx, collectionID, recordsContent)
	if err != nil {
		log.Error("error pushing logs", zap.Error(err))
		return nil, grpcutils.BuildInternalGrpcError("error pushing logs")
	}
	res.RecordCount = int32(recordCount)
	log.Info("PushLogs success", zap.String("collectionID", req.CollectionId), zap.Int("recordCount", recordCount))
	return res, nil
}

func (s *Server) PullLogs(ctx context.Context, req *logservicepb.PullLogsRequest) (*logservicepb.PullLogsResponse, error) {
	res := &logservicepb.PullLogsResponse{}
	collectionID, err := types.ToUniqueID(&req.CollectionId)
	err = grpcutils.BuildErrorForCollectionId(collectionID, err)
	if err != nil {
		return nil, err
	}
	records := make([]*coordinatorpb.SubmitEmbeddingRecord, 0)
	recordLogs, err := s.logService.PullLogs(ctx, collectionID, req.GetStartFromId(), int(req.BatchSize))
	for index := range recordLogs {
		record := &coordinatorpb.SubmitEmbeddingRecord{}
		if err := proto.Unmarshal(*recordLogs[index].Record, record); err != nil {
			log.Error("Unmarshal error", zap.Error(err))
			grpcError, err := grpcutils.BuildInvalidArgumentGrpcError("records", "marshaling error")
			if err != nil {
				return nil, err
			}
			return nil, grpcError
		}
		records = append(records, record)
	}
	res.Records = records
	log.Info("PullLogs success", zap.String("collectionID", req.CollectionId), zap.Int("recordCount", len(records)))
	return res, nil
}
