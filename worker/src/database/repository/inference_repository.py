from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models.inference_entity import InferenceEntity
from src.abstract.builder.inference_entity_builder import InferenceEntityBuilder
from src.database.models.input_entity import InputEntity
from src.database.models.model_entity import ModelEntity
import src.database.repository.input_repository as input_repository
import src.database.repository.model_repository as model_repository

async def add(
  session: AsyncSession,
  model_name: str,
  req_id: str,
  input_content: str,
  predict_label: str,
  score: float,
  inference_time: float,
  ) -> InferenceEntity:
    
  print(f'[REPOSITORY]: Writing to disk', flush=True)
  model_entity: ModelEntity = await model_repository.find_or_create(session, model_name)
  input_entity: InputEntity = await input_repository.add(session, req_id, input_content)

  record = InferenceEntityBuilder \
    .create() \
    .withModelId(model_entity.id) \
    .withInputId(input_entity.id) \
    .withRequestId(req_id) \
    .withPredictionContent(predict_label) \
    .withPredictionScore(score) \
    .withInferenceTimeMs(inference_time) \
    .build()
    
  session.add(record)
  await session.commit()

  return record
